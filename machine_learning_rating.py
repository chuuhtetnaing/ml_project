import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from joblib import dump
from joblib import load




class FeatureSelector( BaseEstimator, TransformerMixin ):
    #Class Constructor 
    def __init__( self, feature_names ):
        self._feature_names = feature_names 
    
    #Return self nothing else to do here    
    def fit( self, X, y = None ):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform( self, X, y = None ):
        return X[ self._feature_names ] 

class DateTimeTransformer( BaseEstimator, TransformerMixin ):
    #Class constructor method that takes in a list of values as its argument
    def __init__(self, use_dates = ['year', 'month', 'day'] ):
        self._use_dates = use_dates
        
    #Return self nothing else to do here
    def fit( self, X, y = None  ):
        return self
    
    #Transformer method we wrote for this transformer 
    def transform(self, X , y = None ):
        X.loc[:,'Last Updated'] = pd.to_datetime(X['Last Updated']).copy()
        X.loc[:,'Last Updated'] = X['Last Updated'].astype('int64').copy()
        return X


class AndroidVersionTransformer( BaseEstimator, TransformerMixin ):
    #Class constructor method that takes in a list of values as its argument
    
    #Return self nothing else to do here
    def __init__(self):
        None

    def fit( self, X, y = None  ):
        return self
    
    def android_ver_into_category(self, obj):
        first_char = list(obj)[0]
        try:
            int_value = int(first_char)
            return int_value
        except:
            return 0
    
    #Transformer method we wrote for this transformer 
    def transform(self, X , y = None ):
        X.loc[:,'Android Ver'] = X['Android Ver'].apply(self.android_ver_into_category).copy()
        return X


class NumericalTransformer(BaseEstimator, TransformerMixin):
    #Class Constructor
    def __init__( self, bath_per_bed = True, years_old = True ):
        self._bath_per_bed = bath_per_bed
        self._years_old = years_old
        
    #Return self, nothing else to do here
    def fit( self, X, y = None ):
        return self 
    
    def price_to_float(self, obj):
#         print(obj)
        result = float(''.join(obj.split('$')))
        return result

    def install_count_string_to_numeric(self, obj):
        result = ''.join(obj.split('+')[0].split(','))
        return result

    def size_to_k_numeric(self, obj):
        result = 0.0

        if 'M' in list(obj):
            numeric = ''.join(obj.split('M'))
            result = float(numeric) * 1000
        elif 'k' in list(obj):
            numeric = ''.join(obj.split('k'))
            result = float(numeric)
        else:
            result = 0.0
        return result
    
    #Custom transform method we wrote that creates aformentioned features and drops redundant ones 
    def transform(self, X, y = None):
        X.loc[:,'Size'] = X['Size'].apply(self.size_to_k_numeric).copy()
        X.loc[:,'Installs'] = X['Installs'].apply(self.install_count_string_to_numeric).copy()
        X.loc[:,'Price'] = X['Price'].apply(self.price_to_float).copy()
        return X



class Model():
	def predict(self, X):
		return self.full_pipeline_m_sd.predict(X)
	def __init__(self, X, y=None):
		self.X = X
		self.y = y
		#Categrical features to pass down the categorical pipeline 
		self.categorical_features = ['Category', 'Content Rating', 'Android Ver', 'Type']
		#Numerical features to pass down the numerical pipeline 
		self.numerical_features = ['Size', 'Installs', 'Price', 'Reviews']
		self.datetime_features = ['Last Updated']


		self.categorical_pipeline_sd = Pipeline( steps = [ ( 'cat_selector', FeatureSelector(self.categorical_features) ),
		                                          ( 'android_ver', AndroidVersionTransformer() ),
		                                         ( 'label_encoder', OrdinalEncoder() ),
		                                         ('standard_scaler', StandardScaler())] )
		    
		#Defining the steps in the numerical pipeline     
		self.numerical_pipeline_sd = Pipeline( steps = [ ( 'num_selector', FeatureSelector(self.numerical_features) ),
		                                  ( 'num_transformer', NumericalTransformer() ),
		                                     ('standard_scaler', StandardScaler())
		                                       ] )

		self.datetime_pipeline_sd = Pipeline(steps = [( 'date_selector', FeatureSelector(self.datetime_features) ),
		                                        ( 'cat_transformer', DateTimeTransformer() ),
		                                     ('standard_scaler', StandardScaler())] )


		self.full_pipeline_sd = FeatureUnion( transformer_list = [ ( 'categorical_pipeline', self.categorical_pipeline_sd ), 
		                                                  ( 'numerical_pipeline', self.numerical_pipeline_sd ),
		                                                 ('datetime_pipeline', self.datetime_pipeline_sd)
		                                                 ])
		self.full_pipeline_m_sd = Pipeline( steps = [ ( 'full_pipeline', self.full_pipeline_sd),
		                                  
		                                  ( 'model', LinearRegression() ) ] )
		self.full_pipeline_m_sd.fit(self.X,self.y)

	


