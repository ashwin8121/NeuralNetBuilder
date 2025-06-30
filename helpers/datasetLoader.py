from PyQt6.QtCore import QThread, pyqtSignal
from sympy.physics.vector.printing import params
from tensorflow.keras.preprocessing.image import ImageDataGenerator, DirectoryIterator



class DatasetLoader(QThread):
    loading_completed = pyqtSignal()
    def getImageDataset(self, datasetPath, params, rescale=None) -> DirectoryIterator:
        self.datasetPath = datasetPath
        self.params = params
        self.dataGen = ImageDataGenerator(rescale=1/255. if rescale else None,)

    def run(self):
        self.dataset = self.dataGen.flow_from_directory(
            self.datasetPath,
            batch_size=self.params["batchSize"],
            class_mode=self.params["classType"].lower(),
            target_size=self.params["imageSize"],
            color_mode=self.params["colorMode"].lower(),
            shuffle=self.params["shuffle"],
            seed=self.params["seed"]
        )
        self.loading_completed.emit()




# def getDatasetMetaData(dataGen: DirectoryIterator):
