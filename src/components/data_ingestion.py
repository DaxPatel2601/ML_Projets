import os 
import sys 
from src.exception import CustomException
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
# from src.logger import logging 


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw_data.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        # logging.info("Entered the Data Ingestion Method")
        
        try:
            # Data Collection and convert into Pandas DataFrame
            df=pd.read_csv("notebook\data\stud.csv")
            # logging.info("Dataset Loaded into DataFrame")
            
            
            # make Directory 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            # save Raw data into relevant path
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            
            # logging.info("Train Test Split initiate")
            train_set , test_set = train_test_split(df,test_size=0.20,random_state=42)
            
            # Save Training data into relevant location
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
            # save Test data into relevant location 
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            # logging.info("Ingestion of the data is completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_set
                )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()