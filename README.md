# Forest Fire Detection ML Model

This project is a machine learning model for forest fire detection that predicts the probability of a forest fire occurring in a given area. The model is trained on a dataset of environmental variables such as temperature, humidity, wind speed, and other factors that contribute to the likelihood of a forest fire.

## Installation

To run the project, you will need Python 3 and the following libraries:

- numpy
- pandas
- scikit-learn

To install the required libraries, run the following command:

`pip install -r requirements.txt`


## Usage

To use the model, simply run the `predict.py` script and provide the environmental variables as command line arguments. For example:

`python predict.py --temperature 25 --humidity 70 --oxygen 10`


This will output the probability of a forest fire occurring based on the provided variables.

## Dataset

The dataset used to train the model is included in the `data` directory. It consists of environmental variables and binary labels indicating whether a forest fire occurred in a given area.

## Model

The machine learning model used in this project is a logistic regression classifier, trained on the dataset described above. The model achieves an accuracy of over 90% on the test set.

## Future Work

In the future, we plan to improve the model's accuracy by incorporating more environmental variables and exploring other machine learning algorithms. We also plan to deploy the model as a web service to make it more accessible to users.

## Contributors

- Vishal Raj
- Vedant Shinde

## Website Link

[Forest Fire Detection](http://vedantshinde.pythonanywhere.com/)
