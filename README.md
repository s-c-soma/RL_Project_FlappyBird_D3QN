# RL Project: Training Flappy Bird using Double Dueling Deep Q Network [D3QN]

![Gameplay](https://github.com/s-c-soma/flappy-bird-deep-q-learning/blob/master/screenshots/gameplay.gif)


## Summary
Flappy Bird was a popular iOS and Andorid game between 2013 and 2014. The was a side-scrolling game that had the user flap the birds wings to get past as many obstacles as possible. For every avoided obstacle the user would earn one point, acumulating to the total score. 

This repository contains the source code to train a deep reinforcement learning model to play the flappy bird game and attempt to reach a high score. For this project we decided to use Dueling Double Deep Q Network (D3QN) with prioritized experience replay. 

In this repository you will find
  - Python Source Code
  - Results
  - Google Colabs
  - Screenshots
  - Model


## D3QN Network
![D3QN Network](https://cdn-images-1.medium.com/max/1200/1*FkHqwA2eSGixdS-3dvVoMA.png)

## Folder Structure and Files 
    .
    ├── assets                                                  # Contains the required audio and image files
    ├── colab                                                   # Contains the colab files
    │   ├── Flappy_DoubleDueling_DQN.ipynb                      # Colab for training model in local Jupyter Noebook
    │   └── Flappy_DoubleDueling_DQN_GoogleColab.ipynb          # Colab for training model in Google colab and code from Google Drive
    ├── cuda_check                                              
    │   └── cuda_check.py                                       # File to check local cuda setup
    ├── game                                                    # Contains the code for Flappy Bird set up with Pygame
    │   ├── flappy_utils.py                      
    │   └── flappy_wrapped.py          
    ├── model                                              
    │   └── infinity_flappy_bird_model.dat                             # Infinity Glappy Bird agent model trained with D3QN 
    ├── result_csv                                              
    │   └── d3qn_mean reward.csv                                # CSV file containing Mean Reward from D3QN Best Model
    ├── screenshots                                             # Contains Gif file used in readme file
    ├── runs                                                    # Tesnorboard log files
    ├── documents                                               # Contains ppt presentation and project report
    ├── play_game.py                                            # Python file to run the model from 'model' folder
    └── README.md

## Setup Environment
For environment setup please use Python version 3.x.x and setup the required packages from requirements.txt
> pip install -r requirements.txt

## Training Model in Jupyter Notebook and Tensorboard Setup
To Train the model from Jupyter Notebook please go to the root folder and start Jupyter Nootbook using the following command
> Jupyter Notebook

Start the TensorBoard executing the following command:
>tensorboard --logdir runs --host localhost

Then go to your browser and open:
> http://localhost:6006

Excecute the colab:
> Flappy_DoubleDueling_DQN.ipynb

## Running The Game
Execute the following command to run the trained model from 'model' folder. Here '--model' indicates the location of saved D3QN model.
> python play_game.py --model model/1_best_flappy_model.dat

## Training Result
![Training Plot](https://github.com/s-c-soma/RL_Project_FlappyBird_D3QN/blob/main/screenshots/d3qn_trainingplot.png?raw=true "D3QN Training Plot for Infinity Model")


## Acknowledements
