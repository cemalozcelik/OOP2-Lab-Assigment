from tkinter.tix import Tree
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel
import sys

from numpy import PZERO
from app import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPaintDevice, QPixmap
from skimage import img_as_ubyte
from menu import Menu
from skimage import data

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.source_width = (self.input.geometry().width())
        self.source_height = (self.input.geometry().height())

        #GroupBox : Source
        #Open file
        self.pushButton_actionOpen_Source.clicked.connect(self.open_file)
        self.actionOpen_Source.triggered.connect(self.open_file)
        #Expor As source
        self.actionExport_As_Source.triggered.connect(self.export_as_source)
        self.pushButton_actionExport_As_Source.clicked.connect(self.export_as_source)
        #Clear the source
        self.actionSource_clear.triggered.connect(self.clear_source)
        self.pushButton_actionSource_clear.clicked.connect(self.clear_source)
        #Clear the output
        self.actionOutput_clear.triggered.connect(self.clear_output)
        self.pushButton_actionOutput_clear.clicked.connect(self.clear_output)
        #GroupBox : Output
        #save output
        self.actionSave_Output.triggered.connect(self.save_output)
        self.pushButton_actionSave_Output.clicked.connect(self.save_output)
        #save as output
        self.actionSave_As_Output.triggered.connect(self.save_as_output)
        self.pushButton_actionSave_As_Output.clicked.connect(self.save_as_output)
        #Export as output
        self.actionExport_As_Output.triggered.connect(self.export_as_output)
        self.pushButton_actionExport_As_Output.clicked.connect(self.export_as_output)
        #Undo
        self.actionUndo_Output.triggered.connect(self.undo_output)
        self.pushButton_actionUndo_Output.clicked.connect(self.undo_output)
        #Redo
        self.actionRedo_Output.triggered.connect(self.redo_output)
        self.pushButton_actionRedo_Output.clicked.connect(self.redo_output)
        
        #GroupBox : Conversion
        #RGB to Grayscale
        self.actionRGB_to_Grayscale.triggered.connect(self.rgb_to_grayscale)
        self.pushButton_actionRGB_to_Grayscale.clicked.connect(self.rgb_to_grayscale)
        #RGB to HSV
        self.actionRGB_to_HSV.triggered.connect(self.rgb_to_hsv)
        self.pushButton_actionRGB_to_HSV.clicked.connect(self.rgb_to_hsv)
        
        #GroupBox : Segmentation
        #Multi otsu
        self.actionMulti_Otsu_Thresholding.triggered.connect(self.multi_otsu_thresholding)
        self.pushButton_actionMulti_Otsu_Thresholding.clicked.connect(self.multi_otsu_thresholding)
        #Chan-Vese Segmentation
        self.actionChan_Vese_Segmentation.triggered.connect(self.chan_vese_segmentation)
        self.pushButton_actionChan_Vese_Segmentation.clicked.connect(self.chan_vese_segmentation)
        #Morphological Snakes
        self.actionMorphological_Snakes.triggered.connect(self.morphological_snakes)
        self.pushButton_actionMorphological_Snakes.clicked.connect(self.morphological_snakes)
        
        #GroupBox : Edge Detection
        #Roberts
        self.actionRoberts.triggered.connect(self.roberts_edge_detection)
        self.pushButton_actionRoberts.clicked.connect(self.roberts_edge_detection)
        #Sobel
        self.actionSobel.triggered.connect(self.sobel_edge_detection)
        self.pushButton_actionSobel.clicked.connect(self.sobel_edge_detection)
        #Scharr
        self.actionScharr.triggered.connect(self.scharr_edge_detection)
        self.pushButton_actionScharr.clicked.connect(self.scharr_edge_detection)
        #Prewitt
        self.actionPrewitt.triggered.connect(self.prewitt_edge_detection)
        self.pushButton_actionPrewitt.clicked.connect(self.prewitt_edge_detection)
        
    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Images (*.png *.jpg)", options=options)
        if fileName:
            self.image_path = fileName
            self.image_menu = Menu(self.image_path)
            self.set_source_label(self.image_path)
    
    def setEnable_openfile(self,bool):

        self.actionRGB_to_Grayscale.setEnabled(bool)
        self.pushButton_actionRGB_to_Grayscale.setEnabled(bool)
        self.actionRGB_to_HSV.setEnabled(bool)
        self.pushButton_actionRGB_to_HSV.setEnabled(bool)
        self.actionExport_As_Source.setEnabled(bool)
        self.pushButton_actionExport_As_Source.setEnabled(bool)
        self.actionSource_clear.setEnabled(bool)
        self.pushButton_actionSource_clear.setEnabled(bool)
        self.actionMulti_Otsu_Thresholding.setEnabled(bool)
        self.pushButton_actionMulti_Otsu_Thresholding.setEnabled(bool)
        self.actionChan_Vese_Segmentation.setEnabled(bool)
        self.pushButton_actionChan_Vese_Segmentation.setEnabled(bool)
        self.actionMorphological_Snakes.setEnabled(bool)
        self.pushButton_actionMorphological_Snakes.setEnabled(bool)
        self.actionSobel.setEnabled(bool)
        self.pushButton_actionSobel.setEnabled(bool)
        self.actionRoberts.setEnabled(bool)
        self.pushButton_actionRoberts.setEnabled(bool)
        self.actionScharr.setEnabled(bool)
        self.pushButton_actionScharr.setEnabled(bool)
        self.actionPrewitt.setEnabled(bool)
        self.pushButton_actionPrewitt.setEnabled(bool)
    
    def setEnable_after_action(self,bool):
        self.actionSave_Output.setEnabled(bool)
        self.pushButton_actionSave_Output.setEnabled(bool)
        self.actionSave_As_Output.setEnabled(bool)
        self.pushButton_actionSave_As_Output.setEnabled(bool)
        self.actionExport_As_Output.setEnabled(bool)
        self.pushButton_actionExport_As_Output.setEnabled(bool)
        self.actionOutput_clear.setEnabled(bool)
        self.pushButton_actionOutput_clear.setEnabled(bool)
    
    def set_source_label(self,source):
        pixmap = QPixmap(source)
        self.setEnable_openfile(True)
        self.groupBox_input.setMinimumSize(pixmap.width(),pixmap.height())
        self.input.setPixmap(pixmap)

    def set_output_label_copied(self,output):
        pixmap = QPixmap(output)
        self.groupBox_output.setMinimumSize(pixmap.width(),pixmap.height())

        self.output.setPixmap((pixmap))
        self.setEnable_after_action(True)
    
    def export_as_source(self):
        self.image_menu.export_as_source()
    def clear_source(self):
        self.input.clear()
        self.setEnable_openfile(False)
    def clear_output(self):
        self.output.clear()
        self.setEnable_after_action(False)
    def save_output(self):
        self.image_menu.save_output()
    def save_as_output(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "Images (*.png *.jpg)", options=options)
        if fileName:
            self.image_menu.save_as_output(self.image_output, fileName)
            
    def export_as_output(self):
        self.image_menu.export_as_output(self.image_output)
    def undo_output(self):
        pass
    def redo_output(self):
        pass
    def rgb_to_grayscale(self):
        self.image_output = self.image_menu.rgb_to_gray()
        #self.set_output_label(self.image_output,QtGui.QImage.Format_RGB888)
        self.set_output_label_copied(self.image_output)
        
    def rgb_to_hsv(self):
        self.image_output = self.image_menu.rgb_to_hsv()
        self.set_output_label_copied(self.image_output)
        
    def multi_otsu_thresholding(self):
        self.image_output = self.image_menu.multi_otsu_thresholding()
        self.set_output_label_copied(self.image_output)
        
    def chan_vese_segmentation(self):
        self.image_output = self.image_menu.chan_vese_segmentation()
        self.set_output_label_copied(self.image_output)
    def morphological_snakes(self):
        self.image_output = self.image_menu.morphological_snakes()
        self.set_output_label_copied(self.image_output)
    
    def roberts_edge_detection(self):
        self.image_output = self.image_menu.roberts_edge_detection()
        self.set_output_label_copied(self.image_output)
    def sobel_edge_detection(self):
        self.image_output = self.image_menu.sobel_edge_detection()
        self.set_output_label_copied(self.image_output)
    def scharr_edge_detection(self):
        self.image_output = self.image_menu.scharr_edge_detection()
        self.set_output_label_copied(self.image_output)
    def prewitt_edge_detection(self):
        self.image_output = self.image_menu.prewitt_edge_detection()
        self.set_output_label_copied(self.image_output)

if __name__ == "__main__":
    app = QApplication([])
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())