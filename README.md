# Pong Lab: ML Player

## Introduction
Create an AI agent for the single player Pong-like game.

## Steps

1. Create your own training file:  
Make sure to set  `train = True` around lab4.py line 94 to record your states.  
Play the game until you have a satisfying csv recording. 

2. Train: 
- Look at your csv and decide on your ML model:  
	Supervised/unsupervised?  
	Classification / regression / clustering?  
	https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

- Create a separate notebook/script:  
Create X/y matrices: What should be your features vs output?  
See 5.2/12a: X_iris/y_iris setup via pd.drop()  
Train and save your ML model  
See class examples or [dsexample](https://github.com/memoatwit/dsexample/blob/master/Insurance%20-%20Model%20Training%20Notebook.ipynb)  
Save your model to be used in the game:
```python
	from joblib import dump, load 
	dump(clf, 'mymodel.joblib') #save  
	clf2 = load('mymodel.joblib')  #load
```
3. Deploy:  
Go back to lab4.py, set `train = False` and complete the logic around line 150 to predict the next moving direction for the paddle. 

## Example
Here are two different types fo models from two different training sets playing solo:

![ml1 screenshot](./pong_ml1.gif)

![ml2 screenshot](./pong_ml2.gif)

