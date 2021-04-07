<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="GUI/Images/logo.png" alt="Logo" width="580" height="200">
  </a>

  <h3 align="center">RISC-V Simulator</h3>

  <p align="center">
    A python implementation of RISC-V Simulation.
    <br />
    <a href="https://github.com/tanmayaeron/CS204_Project_RISC-V"><strong>Explore the docs »</strong></a>
    
  </p>
</p>




<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#contributors">Contributors</a></li>
      </ul>
    </li>
    <li>
      <a href="">Getting Started</a>
      <ul>
        <li><a href="#libraries-used">Libraries Used</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


The aim of this project is to simulate the machine level execution of RISC V 32-bit instructions using a high level language.\\

The Project also aims to give updates to the user regarding each step of the execution of the program. It also returns the final status of the memory and registers as output for the user to analyse the working of their programs thoroughly.
The Project currently allows the user to use 29 different instructions and can be extended to allow the use of any number of instructions by editing the .csv files as long as the instructions are supported by 32-bit RISC V ISA.
For each instruction the program gives various updates like IR, PC, decoded instruction, temporary registers like RA, RB, RZ, RY, etc. during each cycle and prints the number of cycles.
The program executes each instruction using five stages as described in the RISC V architecture.



## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python (>3.7)
* pip (>21.0.3)

### Libraries Used
#### Back-end - Python3
* <b>pandas: </b> for reading .csv files.
* <b>os: </b> for getting and adding path to certain file locations.
* <b>defaultdict: </b> to make a hash map for memory.
* <b> sys: </b> for reading and editing files with ease.

#### Front-end - Python3
* <b>PyQT5: </b> for the Graphic User Interface.
* <b>qdarkstyle: </b> for dark theme

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```JS
   const API_KEY = 'ENTER YOUR API';
   ```




### Contributors
* Aditya Agarwal - 2019CSB1064
* Aneeket Mangal - 2019CSB1071
* Fadia Het Rakeshkumar - 2019CSB1084
* Shikhar Soni - 2019CSB1119
* Tanmay Aeron - 2019CSB1124
    
     
 
