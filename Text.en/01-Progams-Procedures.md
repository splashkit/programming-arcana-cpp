# Level 1: Programs and Procedures #

Welcome to the Programming Arcana! This book aims to help you learn how to **read**, **write** and **understand** code. Learning to code is a journey in which you will explore the secret and mystical world of the computer. Through this journey you will learn to take control of todays powerful and ever present computing devices. This volume is the start of that journey, and will set you up to engage with the more powerful tools presented in the next volume.

At the end of the journey you will have developed a good understanding of the fundamentals of many programming languages. Specifically, you will be able to do the following:

1. Setup a computer with the tools necessary to create your own programs.
1. Read and understand code written by others, and be able to explain how their code works and what it achieves.
1. Write code using structured programming techniques.
1. Use the command line and developer tools to compile, run, and test programs.
1. Design the structure of programs using modular and functional decomposition.

We are going to get started straight away, but if you want some more details about this book checkout the [About Appendix](#about).

<note>
<header>Already Setup?</header>
It is always good to know how to setup your own compter, but if someone else has already setup your computer you can skip the installation instructions and move on to the [next section](#understanding-code).
</note>

## Getting Started ##

What is the first thing that any starting coding wizard needs? A working computer setup with developer tools.

Regardless of the kind of programming you are going to do, there are usually a number of tools that you need to install. We are going to start off using basic tools, which means you have to do a little more work yourself but does means that the skills you learn are likely to help you across a wide range of programming languages and tools. Keeping the tools simple also helps us focus on the really important aspects: understanding and writing code.

To get started you are going to need the following tools:
* A **Text Editor** into which you will type your program's code.
* A Command Line **Terminal** in which you will run the compiler and the programs you create.
* A **Compiler** that will convert your code into programs the computer can run.

### Text Editors and Syntax Highlighting ###

When you are coding you will spend much of your time in a *Text Editor*. The best kinds of editors for code include **syntax highlighting** where the editor uses details about the programming language to color parts of the code as you write it. This makes it much easier to find and fix small errors as you go.

There are many different syntax highlighting text editors, each will support different programming languages and operating systems. Fortunately there is now one that works well across all operating systems, covers a good range of programming languages, is extensible, easy to use, and best of all... its free! This is the **Atom** text editor. You can download Atom and install it from [Atom.io](https://atom.io).

![Visit [Atom.io](https://atom.io) and follow their instructions to download and install the Atom text editor.](./Figures/01-program-procedure/02-atom-site.png){width=500px}

<task>
<header>Download and Install Atom</header>
Before continuing, make sure that you have Atom installed. Follow the steps from the [Atom website](https://atom.io).

1. Open your web browser
2. Navigate to https://atom.io
3. Download and install Atom
</task>

### Command Line Terminal ###

Next, we need an environment from which we can issue commands to the computer. For this you will need to install a Command Line **Terminal**. This is a text based tool that lets you type instructions that run and interact with programs on your computer. Learning to use the command line will be an important skill as you work with more advanced tools.

The great news is that if you are using Linux or MacOS, you already have a command line that is ready to go!

* On Ubuntu Linux you can find the Terminal in the *Accessories* folder within *Applications*.
* MacOS you can find the Terminal in the *Utilities* folder within *Applications*.

Windows does have its own command line, but we are going to need a Unix command line (like with Linux and MacOS). For this you will need to either install a new terminal, or update the one built into Windows.

* **Option 1**: Install Bash for Windows 10.

    This uses an officially supported version of Bash (the Unix terminal) but still uses the standard Windows Command Line Terminal. Unfortunately this Terminal is very limited, and makes it hard to do simple things like Copy and Paste.

    For details on how to set this up have a look at [How to Install and Use the Linux Bash Shell on Windows 10](http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/) article. If you are choosing this option, follow the steps in this article to setup your machine.

* **Option 2**: Install **MSys2** for Windows.

    This is a 3rd party package which also adds a Bash command line and the related Unix tools to Windows. Its free and comes with a very usable Terminal.

    If you choose this option, follow the steps from the [MSys2 website](https://msys2.github.io).


<task>
<header>Setup and Open the Terminal</header>
If you have Linux or MacOS, locate and open your Terminal program. On Windows, either install MSys2 or setup Bash using the above options.

1. Install or locate the Terminal program
2. Run the terminal program and have it open and ready for the next step!
</task>

### Installing a Compiler ###

The next tool you need is a **compiler**. You will use the compiler to convert your program's source code into an executable file that the users can run. We are going to use a compiler called *clang*. How you install *clang* will depend on your operating system, so jump ahead to the instructions for [Linux](installing-clang-on-linux), [MacOS](installing-clang-on-macos), or [Windows](installing-clang-on-windows).

#### Installing Clang on Linux ####

Installing clang on Linux will depend on your distribution. Generally it should be as easy entering a few commands in the Terminal.

Open the terminal and enter the following commands:

```bash
sudo apt-get update
sudo apt-get install clang
```

#### Installing Clang on MacOS ####

Installing clang on MacOS requires you to run the following command in the Terminal:

```bash
code
```

#### Installing Clang on Windows ####


### Creating Your First Program ###

### Customising Your Dev Environment ###



<!-- <video
   src="https://cfvod.kaltura.com/pd/p/691292/sp/69129200/serveFlavor/entryId/0_1whw5ogz/v/2/flavorId/0_ffjvk2cg/fileName/Programs_and_procedures_(Swinburne_CodeCasts_-_Introduction_to_Programming_in_Pascal_1.4)_-_HD.mp4/name/a.mp4"
   controls="controls"
   width="560"
   height="315">
</video> -->





## Understanding Code ##

![The Atom text editor with the code for a Hello World program.](./Figures/01-program-procedure/01-atom-hello-world.png){width=500px}

Computers are powerful, but completely unintelligent, devices.


Conceptual artefacts


Creating a artefact
Instructions that use artefacts
