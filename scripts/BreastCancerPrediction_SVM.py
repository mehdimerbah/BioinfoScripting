
# coding: utf-8

# In[3]:


#Importing some libraries
import sklearn
from sklearn import svm
from sklearn import datasets
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier


# In[31]:


#Loading The dataset
cancer = datasets.load_breast_cancer()


# In[29]:


#Show Features
print("Features: ", cancer.feature_names)


# In[33]:


# Show target labels
print("Labels: ", cancer.target_names)


# In[35]:


x = cancer.data  # All of the features
y = cancer.target  # All of the labels
# X are the values for the different features
# Y is the target (0 for benign and 1 for malignant)
print("Data: \n", x)
print("Labels: \n", y)
#split the data set into training and testing data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)


# In[8]:


print(x_train[:5], y_train[:5])


# In[9]:


classes=['malignant' 'benign']
#didn't need it


# In[39]:


# Assigning classifiers
support_vector_classifier = svm.SVC(kernel='linear',C=2)
knn_classifier = KNeighborsClassifier(n_neighbors=9)

# Training the models
support_vector_classifier.fit(x_train, y_train)
knn_classifier.fit(x_train, y_train)


# In[40]:


# Make some predictions using the test data
svm_predictions = support_vector_classifier.predict(x_test)
knn_predictions = knn_classifier.predict(x_test)


# In[41]:


# Assess the accuracy of the models
svm_acc = metrics.accuracy_score(y_test,svm_predictions)*100
knn_acc = metrics.accuracy_score(y_test,knn_predictions)*100


# In[42]:


print("SVM Prediction Accuracy: %4.3f%%\nKNN Prediction Accuracy: %4.3f%%\n" % (svm_acc, knn_acc)) 


# In[ ]:


# Add Bootsrapping to confirm results

