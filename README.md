# CS 578: Transparent and Interactive Machine Learning - Spring 2019

## Course Description

This course will discuss how we can enable humans and machine learning systems to interact and collaborate for more effective and accurate decision making. Topics include but are not limited to expert systems, recommender systems, active learning, crowdsourcing, learning with rationales, interactive machine learning, and transparency. Students are expected to delve deep into the assumptions, mathematical formulations, and algorithmic optimizations of various machine learning algorithms, read several academic papers, analyze numerous datasets, inspect implicit and explicit biases present in the analytical processes, and build an interactive and transparent machine learning system.

## Course Objectives

1. Provide theoretical, statistical, and mathematical foundations for several machine learning algorithms, including decision trees, naïve Bayes, logistic regression, linear regression, linear and non-linear support vector machines, L2 regularization, L1 regularization, and neural networks.
2. Provide an understanding of the underlying assumptions, strengths, and weaknesses of several machine learning algorithms.
3. Provide an understanding of when implicit and explicit biases might arise due to i) the choice of the machine learning algorithm, ii) the assumptions of the machine learning algorithm, iii) the objective function, iv) the optimization procedure, and v) the dataset itself.
4. Provide a theoretical and practical understanding of how we can enable machine learning algorithms accept both expert and novice feedback.
5. Provide a mathematical foundation of how we can make black-box machine learning algorithms explain their reasonings.
6. Practice the design and implementation of an interactive and transparent decision-making process powered by machine learning algorithms.

## Prerequisites
Required: CS422 and CS430. Also recommended: Math 332 and Math 474.

## Topics
The topics we will cover are as follows. The precise amount of time we will spend on each topic will vary based on student interest and participation.

* Concept learning
  * Inductive bias, version space, Find-S, candidate elimination, active learning
* Probability background
  * Random variables, joint distribution, conditional distribution, chain rule, Bayes rule
* Feature selection and ranking
  * Mutual information
  * Chi2
  * Regularization
* Bayesian networks
  * Representation
  * Structure learning
  * Synthetic data generation
* Decision trees
  * Information gain, overfitting, underfitting, bias versus variance, version space
  * Interactive learning (version space reduction, query-by-bagging)
  * Transparency (visualize the tree, understand how the inductive bias affects the final tree, how to interpret the root and leaves in terms of feature importance)
* Active learning
  * Motivation, uncertainty sampling, query-by-committee sampling, advantages, disadvantages
* Transparency
  * Motivation, aims, applications, approaches
* Linear regression
  * Error functions, maximum likelihood, noise, outliers, closed-form solution to linear regression 
  * Interactive learning (measures of uncertainty for regression, variance-based approaches)
  * Transparency (interpreting the weights, the effect of scaling the features)
* Naïve Bayes
  * Bayes classifier, Bayesian parameter estimation, bias, probability calibration
  * Interactive learning (uncertainty sampling, expected error reduction)
  * Transparency (interpreting the log-ratios as feature weights, understanding the implications of the conditional-independence assumption, inspecting the over-confidence of naïve Bayes)
* Logistic regression
  * The logistic function, gradient optimization
  * Interactive learning (uncertainty sampling)
  * Transparency (interpreting the weights, understanding the effect of joint optimization on the weights of correlated features, the effect of scaling features on the weights)
* Support vector machines (SVMs)
  * The objective function, the linear SVM, the kernels
  * Interactive learning (the active learning for SVMs paper and others)
  * Transparency (approaches to making non-linear SVMs more transparent)
* Neural networks
  * The neural network representation, backpropagation, various architectures, overfitting
  * Interactive learning (multiclass active learning, active learning for neural networks)
  * Transparency (several papers on making neural networks’ decisions more transparent)
* Regularization
  * L2 regularization, L1 regularization, regularization applied to regression and classification
  * Transparency (understanding the general and different effects of L2 and L1 regularization on the weights)
* Recommender systems (RS)
  * Content-based RS, collaborative filtering, matrix factorization
  * Interactive learning (implicit and explicit feedback)
  * Transparency (several papers)
* Interactive machine learning
  * Learning with rationales, tandem learning, visualization
* Crowdsourcing
  * Learning from experts vs. novice users, handling noise, exploration vs. exploitation
* Other topics
  * Expert systems, human-computer interaction, intelligent user interfaces, computer-aided diagnosis, computer-supported cooperative work, chat bots, interacting with robots

## Course Materials
* [Slides](slides)
* [Jupyter Notebooks](notebooks)
* [Reading Materials](reading.md)

## Python
* Python 3.6, 64bit https://www.python.org/
* Jupyter notebook https://jupyter.org/
* Pandas https://pandas.pydata.org/
* Scikit-learn http://scikit-learn.org/stable/ 
* TensorFlow https://www.tensorflow.org/ 
* Keras  https://keras.io/
* Bokeh https://bokeh.pydata.org/en/latest/

## Git & GitHub Cheat Sheets
* Git Cheat Sheets https://education.github.com/git-cheat-sheet-education.pdf
* GitHub Flow Guide https://enterprise.github.com/downloads/en/github-flow-cheatsheet.pdf
* GitHub Markdown Guide https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf

## Other Links
* Bayesian network software - Hugin-lite https://www.hugin.com/index.php/hugin-lite/
