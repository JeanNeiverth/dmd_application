# DMD and SINDy applied to Time-Dependant Schröedinger's Equation

Final project of the Data-Driven Algorithms course for the Control and Automation Engineering BSc at Universidade Federal de Santa Catarina in 2023, second semester.

Credits to Luke Polson for the numerical solver ([Link](https://github.com/lukepolson/youtube_channel/blob/main/Python%20Metaphysics%20Series/vid17.ipynb)).

### Description

As the analytical complexity of quantum physics topics increases, numerical approaches are increasingly used. Two common tasks for data-driven applications in this field are (I) model identification, in order to identify a model based on data and (II) model complexity reduction, to perform simulations with a lower computational cost.

The objectives of this project are:
* Run the numerical solver for Schröedinger’s Equation, in order to acquire data. Perform the algorithm for 5 different initial conditions, being one of them the particular case of the harmonic oscillator;
* Apply DMD to identify systems modes, enabling a less costly approach for simulation;
* Identify Schröedinger’s PDE using SINDy algorithm.

### Results

With DMD, it was possible to reconstruct the original data with a low error (at the order of $10^{-3}$ MAE). The reconstruction quality can also be checked visually.

![reconstruction2](https://github.com/JeanNeiverth/dmd_application/assets/79885562/da6d57aa-397c-421d-85aa-1d289e004e13)

With the reconstruction, it was possible to save around 96% storage size of the time series data.

Also, using SINDy algorithm, it was possible to correctly identify the harmonic oscillator PDE.

### How to use

First, it is necessary to install the libraries in requirements.txt.

The project has 3 main files:
* "generate_data.ipynb", inside of "1_Generate_Data";
* "dmd_project.ipynb", inside of "2_DMD";
* "harmonic_oscillator.ipynb", inside of "3_SINDy";

Running these 3 notebooks in sequence will reproduce the results.

