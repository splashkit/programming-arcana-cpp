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

The next tool you need is a **compiler**. You will use the compiler to convert your program's source code into an executable file that the users can run. We are going to use a compiler called *clang*. How you install *clang* will depend on your operating system, so jump ahead to the instructions for your operating system.

**Linux**: Installing clang on Linux will depend on your distribution. Generally it should be as easy entering a few commands in the Terminal. Open the terminal and enter the following commands:

```bash
sudo apt-get update
sudo apt-get install clang
```

**MacOS**: Installing clang on MacOS requires you to run the following command in the Terminal:

[comment]: <> (TODO: Remove the space between -- and install)

```bash
xcode-select -- install
```

**Windows** How you install clang on Windows depends on the Terminal you are using. If you are using Bash in Windows 10, follow the instructions for installing clang on Linux. If you are using MSys2 then you can install clang using the following command:

```bash
pacman -Sy mingw-w64-x86_64-clang mingw-w64-i686-clang
```

### Installing Splashkit ###

[Splashkit](splashkit.io) is designed to help you get started with programming. It is a library of reusable code that provides tools to help you make more interesting programs. Using Splashkit you will soon be creating small games, responding to command from your own web servers, or interacting with a custom database.

To install Splashkit:

[comment]: <> (TODO: Work out how this works...)

```bash
curl http://splashkit.io/...
```

### Creating Your First Program ###

Ok, now you can create your first program! Wait... before you write your first line of code you need to know that there are gods for each programming language. These gods can be vengeful 🌩if you do not make the right offering as your first program! To please the programming gods you need to create a special program as your first code: "Hello World". 😃

More seriously, Hello World is a great program to start with for any new language or set of tools. This program just outputs the message "Hello World", and makes sure that you have everything setup correctly before you go on and write more complex programs. Watch the following video and use the steps below to create your own Hello World program and check that your setup is good to go.

<!-- <video
   src="https://cfvod.kaltura.com/pd/p/691292/sp/69129200/serveFlavor/entryId/0_1whw5ogz/v/2/flavorId/0_ffjvk2cg/fileName/Programs_and_procedures_(Swinburne_CodeCasts_-_Introduction_to_Programming_in_Pascal_1.4)_-_HD.mp4/name/a.mp4"
   controls="controls"
   width="560"
   height="315">
</video> -->

1. Open Atom -- you will use this to enter the program's code.
2. Type in the following code. Make sure the text is the same, but do not worry if the colors are different.

    ```c
    #include "splashkit.h"
    #include "splashkit_starter.h"

    void main()
    {
      println("Hello World!");
    }
    ```
3. Save your program as **HelloWorld.cpp** in your Documents folder, or somewhere else on your computer.
4. Switch to the terminal.
5. Tell the terminal that you want to move into the folder where you save the code.

    Think of the terminal as currently being located within a folder on your computer. To get access to files you want to be in the folder where the files are located. So you need to **change** into that folder. To do this you use the **cd** command. This stands for **change directory** and is used to move the location of the Terminal to that folder.

    <note>*Directory* is the technical name for a folder.</note>

    For example: if I saved *HelloWorld.cpp* to a folder named *code* in my documents, I would move into that folder using the following commands. This will move into the *Users* folder, then into the *acain* in Users, then into my *Documents* folder and finally into the *code* folder.

    My username is "*acain*", so on Mac and Linux I would use:
    ```bash
    cd /Users/acain/Documents/code
    ```

    On Windows I would use:
    ```bash
    cd /c/Users/acain/Documents/code
    ```

    <note>Beware of usernames with spaces! If you have a space in your username, then you need to put a backslash (\\) before that space. So if my username was "*andrew cain*" then on Windows I would need to use ```cd /c/Users/andrew\ cain/Documents/code```, the same applies on Mac and Linux. It is generally best to avoid using spaces in folder names.</note>

5. List the files in the current directory using the **ls** command. Check that you can see the *HelloWorld.cpp* file in the listing.
5. Compile and run your program.

    To do this you need to run the *clang++* program and pass it some options so it knows you want to use Splashkit and you want to compile the HelloWorld.cpp file.

    ```bash
    clang++ `splashkit -cpp-starter` HelloWorld.cpp -o HelloWorld
    ```

    When this runs successfully it will not print anything out, but it should have created a program that you can see in the folder (and using *ls* in the Terminal).

    <note>
    Make sure you have the right quotes around the ``` `splashkit -cpp-starter` ```. These are back-ticks and are usually located above the tab key on the left of the keyboard.
    </note>
5. Run your program using:

    ```bash
    ./HelloWorld
    ```

    When this runs it should echo the text "Hello World".

![The Atom text editor with the code for a Hello World program.](./Figures/01-program-procedure/01-atom-hello-world.png){width=500px}


<note>
<header>Code Color Scheme</header>
We are using the **Atom Dark** UI Theme and the **Monokai** Syntax Theme in Atom. You can change your themes in Atom's settings/preferences. The Monokai theme needs to be installed as a custom theme.
</note>



## Computers and Programs ##

Now that you have the tools ready to go, its time to start thinking about code. For that we need to step back and understand a little about programs and compters.

Computers are powerful, but completely unintelligent, devices. Each computer is made up of a number of components, as illustrated in [@Fig:figComputer].

![A computer is made up of a number of components controlled by a central processing unit.](./Figures/01-program-procedure/Computer.png){#fig:figComputer width=500px}

* **Processor**: Each computer has a central processing unit (CPU) that is responsible for performing actions. The CPU responds to instructions that tell it what actions to perform. Each action is very small, but the CPU can perform millions of these actions every second.
* **Memory**: Accompanying the CPU is a component used to store data known as Random Access Memory or RAM for short. This memory can be quickly accessed by the CPU, and is used to store the instructions for the CPU and the data related to these instructions. While RAM is fast, it does not store data persistently and when the power is turned off the data in RAM is lost.
* **Storage Devices**: To save data more permanently each computer has other storage devices that are slower to access, but are able to store data when the power is off. These devices include devices such as solid state drives, hard disks, DVDs, and USB keys. Data on these devices is usually organised into files and folders, and must be loaded into RAM to be used by the CPU.
* **Input Devices**: In order to respond to user actions, each computer will have a number of input devices. This includes things like keyboards, mice, track pads, touch screens, game controllers, network ports, etc. Each of these devices is turning user actions into data that the CPU can access.
* **Output Devices**: The computer also needs devices that can be used to produce outputs. These include things like displays, speakers, network ports, etc. Each of these devices tasks data from the computer and produces an output of some form.

All of these components work together to make up what we think of as a computer. The CPU follows instructions to take inputs from a range of devices, store and work with data in memory, and produce outputs saved as files on a storage device or communicated with users via output devices. These components are consistent across the wide range of computing devices, whether that is a traditional computer, a mobile device or tablet, or a computer embedded in something like a home, vehicle, robot, or medical equipment.

All of these components work together to enable the computer to perform amazing tasks, and yet none of these devices has any inherent intelligence! CPUs follow instructions, memory and storage devices store data, input devices turn user actions into data, and output devices turn data into a medium for the user to receive. So, where does the intelligent behaviour of the computer come from?

Software drives computers: providing the intelligence that controls the computing hardware. These software programs contain instructions that tell the computer what to do, and it is these programs that contain the intelligence that make computers truely useful. It is therefore, the developers of these programs that are the real power driving the computer hardware. As you learn to code, you are learning how to craft instructions that will get the un-intelligent computing hardware to achieve your goals.

### Programs and Compilers ###

Each program is a list of instructions that tells the computer what to do. The challenge here is that the computer's CPU does not operate on english like text, it operates on *machine code*. These codes are represented as binary numbers (consisting of 1's and 0's) with each instruction performing a basic task, see [@Fig:figMachineCode].

![The CPU operates on *Machine Code*: binary instructions that tell the CPU the action you want it to perform.](./Figures/01-program-procedure/MachineCode.png){#fig:figMachineCode width=500px}

This is where the compiler comes in. The compiler is a tool that converts text into machine code that the computer can execute. To achieve this, the code you write needs to follow the rules of the programming language. This allows the compiler to understand what you want achieved in order for it to create the correct machine code. [@Fig:figCompiler] shows the basic operation of the compiler.

![The compiler converts your source code into machine code the computer can execute.](./Figures/01-program-procedure/Compiler.png){#fig:figCompiler width=500px}


### Source Code Structures ###

The machine code for a typical program may contain millions of very small instructions. In order to work with this we need to organise these instructions in some way so that we can think and work at a higher level. To achieve this, programming languages organise your code around a number of different kinds of artefacts (i.e. things you can create). These artefacts are created and manipulated by the code you write. To understand how to code, means understanding the different kinds of artefacts you can create and the instructions you can use to manipulate these artefacts.

Program code generally consists of the following three aspects:

* Code that **declares** (i.e. creates) an artefact.
* Instructions that command the computer to perform an **action**.
* Instructions for the compiler, to help it locate other artefacts.

[@Fig:figAnnotatedHelloWorld] shows these three aspects for the Hello World program you created earlier. The instructions for the compiler at the top of the code indicate that you want to **include** artefacts declared in the SplashKit from the *splashkit.h* and *splashkit_starter.h* files. The body of the code creates (declares) a single **procedure** named `main`, which has within it instructions for the computer to perform when this code is run.

![The Hello World program contains one artefact, and uses others from the Splashkit library.](./Figures/01-program-procedure/AnnotatedHelloWorld.png){#fig:figAnnotatedHelloWorld width=500px}

Now that we have covered this background material, we can start to learn about the artefacts you can create in code and the actions you can perform on these artefacts.

## Level 1 Artefacts, Actions, and Terminology ##

Compiling programs crafted by others is alright, but the true power of coding can only be realised by learning to craft your own programs. You have seen the tools you need to compile programs from source code, so now lets turn our attention to the study program creation.

Level 1 introduces the artefacts used to create programs, and how you can code these using a programming language. Once you have mastered these concepts you will be able to:

* Code programs that perform a scripted sequence of actions.
* Use the compiler to create a program from your code.
* Run your program and relate its execution to the code you wrote.
* Make use of some artefacts from the SplashKit library to output information in creative ways.

This is your first step in your journey to master the arcane knowledge of coding.

### House Drawing Example Code ###

The following code demonstrates all of the concepts covered in the following section. Have a quick read and see if you can work out what the program does.

```c
/// Program: HouseDrawing
///
/// This program opens a window and draws a picture of a house.

#include "splashkit.h"
#include "splashkit_starter.h"

/// Procedure: draw_house
///
/// This procedure draws a house by calling procedures
/// that fill a rectangle for the walls and a triangle
/// for the roof.
void draw_house()
{
    fill_rectangle(COLOR_GREY, 300, 300, 200, 200);
    fill_triangle(COLOR_RED, 250, 300, 400, 150, 550, 300);
}

/// Procedure: draw_hill
///
/// This procedure draws an ellipse that is half off the
/// bottom of the screen so that it looks like a hill.
void draw_hill()
{
    fill_ellipse(COLOR_BRIGHT_GREEN, 0, 400, 800, 400);
}

/// Procedure: main
///
/// This is where the program starts.
/// Main will open a window, then draw a hill with
/// a house on top before delaying for 5 seconds and
/// then ending.
void main()
{
    open_window("House Drawing", 800, 600);
    clear_screen(COLOR_WHITE);

    draw_hill();
    draw_house();

    refresh_screen(60);
    delay(5000);
}
```

### Program (Artefact) ###

In most software projects the top level *artefact* you are aiming to create is a **program**. Within your software a *program* contains a number of other artefacts, and a starting procedure (the `main` procedure). When the program is executed the `main` procedure is called. The computer will continue to run that program until the main procedure ends, which indicates the end of the program.

When you picture a program, you should see it as a collection of things you have created with a starting procedure. It is a wrapper around the software world that you are creating with your code.

![A program can be run by the user and contains artefacts you have created, and those you have used from libraries. When the program is run, its main procedure is called.](./Figures/01-program-procedure/ProgramConcept.png){#fig:figProgramConcept width=500px}

All of the code in the [House Drawing Example Code] is contained with a single program. When this program is run its `main` procedure is executed, and this contains the instructions to open a window and draw a house on a hill. You should think of the program as containing a number of procedures, where each procedure performs a given task. [@Fig:figHouseDrawingProgramConcept] illustrates how we picture the House Drawing program. It shows the program containing the three procedures declared in the program's code, along with the called procedures from SplashKit.

![The House Drawing Program contains procedures we created for main, and to draw a hill and draw a house. It also contains procedures from SplashKit.](./Figures/01-program-procedure/HouseDrawingCodePictured.png){#fig:figHouseDrawingProgramConcept width=500px}

<note>
<header>Notes on the Program Artefact</header>
* A program is an **artefact**, something you can create in your code.
* [@Fig:figProgramConcept] illustrates the concepts related to the program artefact.
* A program is a programming artefact used to define the steps to perform when the program is run.
* You use a compiler to convert the program's source code into an executable file.
* By declaring a program in your code you are telling the compiler to create a file the user can run (execute).
* The program must have an **entry point** that indicates where the program's instructions start.
* Your program can use artefacts that are coded in a [Library](#library-artefact) or number of libraries.
</note>

### Procedure (Artefact) ###

The computer is unintelligent, so performing anything meaningful requires a large number of instructions. Coding all of these directly in the program would be slow and time consuming. To avoid this programming languages offer the capability to group the instructions needed to perform a task into a **procedure**.

A procedure is a list of instructions that gets the computer to perform a specific task. When a procedure is called it gets control of the computer and runs its instructions in **sequence** following the steps provided in order to achieve its task. Often these steps require data, so the procedure may need to be passed data when it is called. When the procedure finishes its task, control returns back to the code that called the procedure.

![A procedure is a packaged up list of instructions that gets the computer to perform a task.](./Figures/01-program-procedure/ProcedureConcept.png){#fig:figProcedureConcept width=500px}

The [House Drawing Example Code] creates three procedures: `main`, `draw_hill`, and `draw_house`. Each of these procedures contains the instructions needed to perform an individual task. This means that you can call the procedure any time you want that task performed. The code used to create two of these procedures is highlighted in [@Fig:figHouseDrawingProcedures]. You should picture this *entire* block of code as a *single thing*: a procedure.

![The code for the House Drawing Program creates procedures for main, draw hill, and draw house.](./Figures/01-program-procedure/HouseDrawingProcedures.png){#fig:figHouseDrawingProcedures width=500px}

<note>
<header>Comments</header>
Comments are a useful way to document your code. These sections of code are ignored by the compiler and can be used to record notes for the developers reading the code.
</note>

Now the great thing about procedures is that you can usually work out what they do from their name (if they have been designed well). You do not need to worry about the *details* of how a procedure works in order to use one. For example, main in the House Drawing Program calls a procedure named `open window`. We can work out that this is going to open a window without needing to know exactly all of the steps it gets the computer to perform in order to achieve this. This is a very powerful idea, and means that you can focus on just the code for the one procedure you are working on at any one time. So, if you are creating main, you only need to think about how you want themain procedure to work.

When writing your own code, make sure you can clearly see each procedure you are creating. For example,  [@Fig:figPictureAProcedure] shows you all of the code related to the `main` procedure. Keeping this all together helps us to keep this picture in mind.

![With procedures, you can focus on just the procedure you are creating. You can use other procedures without needing to know how they work.](./Figures/01-program-procedure/PictureAProcedure.png){#fig:figPictureAProcedure width=500px}

<note>
<header>Notes on Procedure Artefacts</header>
* A procedure is an **artefact**, something you can create and use in your code.
* [@Fig:figProcedureConcept] shows the key concepts related to procedures.
* A procedure is a programming artefact that packages up the instructions needed to perform a task.
* Each procedure has a name, technically known as an [identifier](#identifier_terminology).
* The instructions within a procedure are run in **sequence**.
* Each [library](#library_artefact) will contain reusable procedures.
* The SplashKit library contains procedures that can draw images on the screen, play sounds, and perform many other tasks.
* Procedures are also known as **subroutines**, **sub-programs**, **methods** or **sub-procedures**.
</note>

### Procedure Call (Action) ###

Once you have access to a procedure, either one that you created or one that you found in a library, you can use this procedure by **calling** it: this is know as a **procedure call** statement.

A procedure call is a kind of [statement](#statement_terminology) that instructs the computer to run the code in a [procedure](#procedure_artefact). The procedure call statement uses the procedure's name to identify which procedure to run, and must pass the required data to the procedure's parameters.

![A procedure call is a statement used to start the execution of a procedure.](./Figures/01-program-procedure/ProcedureCall.png){#fig:figProcedureCall width=500px}

Each of the statements within the three procedures in [House Drawing Example Code] are procedure calls. Main includes a call to procedures named `open_window`, `clear_screen`, `draw_hill`, `draw_house`, `refresh_screen`, and `delay`. The draw_hill procedure calls `fill_ellipse`, while draw_house calls `fill_rectangle` and `fill_triangle`. Only `main`, `draw_hill` and `draw_house` are declared within the program; the other procedures all come from SplashKit. This means that the code that declares these procedures is located within the SplashKit library.

[@Fig:figHouseDrawingStructure] shows a chart that communicates the different procedure calls within the House Drawing Program. The boxes represent the procedures, and the arrows represent the procedure calls. You can see that, for example, the `draw_house` procedure calls the `fill_rectangle` procedure as there is an arrow from the box representing the `draw_house` procedure to the box representing the `fill_rectangle` procedure.

![The House Drawing program includes a number of procedures: some from SplashKit and others created in the program itself.](./Figures/01-program-procedure/HouseDrawingStructure.png){#fig:figHouseDrawingStructure width=600px}

<note>
<header>Notes on Procedure Calls</header>
* A procedure call is an **action** you can get the computer to perform. You can call procedures in the instructions in your code.
* [@Fig:figProcedureCall] shows the key concepts related to the procedure call statement.
* A procedure call is an instruction that starts the execution of a procedure.
* You can call a procedure anywhere you can code a statement.
* Within the call you use the name (the [identifier](@identifier_terminology)) of the [procedure](#procedure_artefact) to indicate which one you want run at this point in the program.
* You place the values you want to pass to the procedure within parenthesis, separated by commas if you need to provide multiple values. These are known as arguments. The value of each argument is calculate as part of an [expression](#expression_terminology) and passed to the matching parameter in the procedure.
* When the procedure ends, the program continues with the next [statement](#statement_terminology) in the calling procedure.
</note>

### Type (Artefact) ###

All values within a program will have a *type* that indicates how the data stored in the computers memory is interpreted by the program. Effectively, the type indicates the kind of data you are working with. There are three basic types of data (*data types*) available in a programming language, these are:

* Textual data can be individual characters to sequences of characters.
    * Sequences of characters are known as **strings** and include data such as `"Fred"`, `"Hello World"`, `"23"`, and `"This is text!"`.
    * You can also have individual **characters** such as `'A'`, `'a'`, `'!'`, `'5'`, `' '`, etc.
* Numbers are either whole numbers or real numbers.
    * Whole numbers are known as **integers** values, and include data such as `1`, `0`, `-5`, and `37`.
    * Real numbers are known as **floating point** values (float for short), examples include `0.5`, `-126.0`, `3.141516`, and `23.981`.


![The main data types in programming languages.](./Figures/01-program-procedure/DataTypes.png){#fig:figDataTypes width=600px}

<note>
<header>Notes on Types</header>
* A type is an *artefact*, there will be a number of existing types that you can use, and later you will see how to create your own types.
* The concepts related to expressions are shown in Figure \ref{fig:program-creation-type}.
* A type is a programming artefact that indicates a kind of data.
* The type determines the basic actions that can be performed on the value.
* The type determines the amount of memory needed to store a value of that kind.
* Whole numbers are usually called *Integers*.
* Real numbers are usually represented as *Floating Point* values. These values have a limited precision, supporting only a certain number of digits of precision.
* Textual values can contain numbers as text characters. For example, the text `"23"` is the character '2' followed by the character '3' - it is not the number 23.
* You can perform mathematic operations on numeric data, but not on textual data.
</note>

### Library (Artefact) ###

A library is a collection of reusable code artefacts. Each programming language has its own standard library, and your programs can make use of the artefacts available in this library. SplashKit is also a library; it contains artefacts such as procedures that help make it easy to create more interesting programs when you start learning to code.

<note>
<header>Notes on Library Artefacts</header>
* A library is an **artefact**, one that contains other reusable artefacts.
* Each library will contain [procedures](#procedure_artefact) you can use to perform different tasks.
* Each language has a standard library with code to perform many commonly performed tasks.
* Other libraries extend the capability of the languages further.
* SplashKit is a library that we created to help you build more interesting programs as you start learning to code.
</note>

### Terminology ###

Part of the challenge in learning to program is learning all of the right terminology. As you learn to develop software it is also important that you start to learn this *special language* that software developers use to discuss their programs. You will find that this terminology is used in many places. It is used in programming texts, error messages from the compiler, in discussions between developers, in discussion boards, blogs, anywhere that developers are discussing software development. Having a clear understanding of this terminology will help you make the most of these resources.

#### Identifier (Terminology) ####

An identifier is the technical term for the text that *identifies* something for the compiler. This includes the **name** of the programming artefacts you create (such as procedures and libraries) as well as other words that have special meaning for the compiler. You will use identifiers when you name the artefact you create, and to select the artefact you want to use in statements.

<note>
<header>Notes on Identifiers</header>
* Each artefact that exists within code will have a name: its identifier.
* An artefact's name is used to identify it when you want to use it.
* The name of a [procedure](#procedure_artefact) is an identifier.
* Other **keywords** are also identifiers. These are words that have special meaning to the compiler. For example, the keyword `#include` is used to access code in a library, and the keyword `void` is used to identify the creation of a procedure.
</note>

#### Statement (Terminology) ####

When you are create a program you define the actions the computer will perform when the program is run. Each of these *actions* is coded as a **statement** within the program's procedures. This style of programming is known as **imperative** programming. Imperative means to give authoritative commands, and that is what we do in our programs. Our programs are lists of **authoritative commands**, statements, that *tell* the computer the actions it is to perform.

<note>
<header>Notes on Statements</header>
* A statement is a *term* used to describe the instructions in your code.
* A statement is a *command*, an instruction to perform an action.
* Each [procedure](#procedure_artefact) has a list of statements that are executed when it is called.
* There are only a few different kinds of statements.
* Each statement has a defined set of actions the computer performs to execute the statement.
* A [procedure call](#procedure_call_action) is a kind of statement that tells the computer to run the code in a [procedure](#procedure_artefact).
</note>

#### Expression (Terminology) ####

Some statements need data. This data can be calculated or provided as a *literal* value in your code. The term **expression** is used in programming to describe the places within each statement where data must be supplied. At run time each expression is evaluated and becomes a value when the statement is executed.

<note>
<header>Notes on Expressions</header>
* All values within a program are calculated as part of an expression.
* An expression is a *term* given to code that calculates a value.
* An expression provides a *value* to be used within a [statement](#statement_terminology).
* The argument values passed to parameters in a [procedure call](#procedure_call_action) are all expressions.
* The expression's value may be calculated or entered directly into the code.
* Calculations can use mathematical operators: + for addition, - for subtraction, * for multiplication, / for division, and parenthesis ( ) for grouping.
* Expressions are evaluated using the BODMAS: expressions are evaluated in the order *B* brackets first, *O* orders (which includes powers and square roots), *DM* for division and multiplication (which are of equal precedence, and are evaluated left-to-right), then *AS* addition and subtraction (of equal precedence, evaluated left-to-right).
* Values entered directly within an expression are known as **literal** values.
</note>

## Language and Grammar ##

Now that you have all of the level 1 concepts, the next step is to see how you can realise these cocepts in programming code. This is where the details of a programming language come in. The concepts apply across many programming languages, but in order to write code you need to know the details of the language you are going to use.

In this book we are going to make use of the **C/C++** programming language. We will combine the low level details of C with some of the more programmer friendly aspects of C++. Toward the end of the book we will then look at how the concepts you have learnt apply across a range of programming languages. Each chapter will present the concepts, and then the related syntax. We recommend you focus on the concepts more than the syntax, but you need to understand both to be effective. However, you are likely to need to learn other languages later on and a good understanding of the underlying concepts will make this process much easier.

### Grammar ###

Programming languages have sets of rules that define *how* you write code so that compilers and related tools can understand what you want to achieve. These rules are know as the language's grammar. To make use of a language grammar, the first thing you need to do is understand what you want to achieve. Once you have a notion of what you want to do, you can plan out your program's structure conceptually and map this to code using the grammar rules.

In this book the syntax rules are expressed using *syntax diagrams*. These diagrams show you the rule of the language visually. To get started, have a look at [@Fig:figIdentifierSyntax]. This diagram shows the rules for writing an [identifier](#identifier_terminology) in C/C++. Here are some notes on how to read and make use of this diagram.

  1. Text found at the start of a line (not contained in a box) is the name of a rule. There are four rules in [@Fig:figIdentifierSyntax]: *identifier*, *letter*, *digit* and *underscore*. (Yes, the grammar really does have rules for everything you can type.)
  2. Arrows show the order in which the parts of the rule are applied. They start at the rule name, and point in the direction you need to follow. Each box pointed to by an arrow represents either another rule to apply, or the text that must written.
  3. Red rectangular boxes on a line indicate points where other rules need to be applied. For example, the *letter* box within the *identifier* rule indicates that if you take this path you apply the *letter* rule at this point.
  4. Grey boxes with rounded corners represent text that must be entered into the code. For example, the small rounded box *A* within the *letter* rule indicates that if you take this path you type the letter *A* at this point in your code.

These rules are a very efficient way of working out how you write the code to do or create something for a given language once you learn to read and work with them. We will always provide example code to illustrate points, but that code only shows one way of doing something. The syntax rules can be used much more creatively, so if you can make use of them you will be able to do much more with the progamming language.

Lets have a go at using the [identifier syntax] to create our own identifier. Imagine you are creating a program and inside this program you want to create a procedure that *draws an image*. As part of creating that procedure you will need to come up with an [identifier](#identifier_terminology) to name it. The name you want to use is *draw image*, as this captures what the procedure does. To work out how to write this in code you need to use the [identifier syntax].

Looking at the syntax diagram you can locate the appropriate rule: the rule to create an *identifier*. Following the lines, the first thing you have is an option to start with either a letter or an underscore. As you want to name this "draw image", you would choose a *letter*. This is a red square box, so there must be a rule for what valid letters are. Now, you probably know what a letter is already, but lets see how you can work this out using the grammar. Locate the *letter* rule a little further down in the diagram, by following the arrow for this rule you can choose from the letters *a* to *z* and *A* to *Z*. To name this procedure "draw image" you would choose `d`. That is the end of the *letter* syntax, so you can move back to where you were in the *identifier* rule.

Following the line in the *identifier* rule, you are now at a junction where you can choose to end the identifier or add in additional letters, digits, and underscores. Calling the procedure `d` would be valid, but it would be poor form as it doesn't really tell us what the procedure does. So you can follow the arrow in the diagram down and through *letter* again to add an `r`: so far we now have `dr`. Notice that after this letter there is the option to loop back, and if you follow this you can add in additional letters etc. Using this we can add in two more letters to give `draw`.

At this point we have an issue. You can't name the procedure "draw image", as the C/C++ language does not support spaces in identifiers. Spaces and other whitespace characters are used to separate things in the code, so they cannot be within an identifier. At this point we have several options as to how we can add in the second word. Firstly you could add in an underscore ( _ ) to separate out the words. This style is known as **snake case** and is what we will use for naming our procedures as this mirrors the style used in the C/C++ standard library. So, following the grammar we can make the procedure's identifier `draw_iamge`. All of the different style options are shown in the following list.

* Using all lowercase with underscores to separate words is known as **snake case** and would result in the identifier being named **draw_image**.
* Starting with a lowercase character and new words with an upper case character is known as **camel case** and would result in the identifier being named **drawImage**.
* Starting each work with an uppercase character is known as  **pascal case** and would give the result **DrawImage**.
* All uppercase characters separated by underscores, gives **DRAW_IMAGE**, and is called uppercase.

## Level 1 C/C++ Syntax ##

### Identifier Syntax ###

The C/C++ [identifier](#identifier_terminology) syntax is shown in [@Fig:figIdentifierSyntax]. In C/C++, as in most programming languages, the identifier must start with a letter or an underscore ( _ ) which may be followed by other letters, numbers, or underscores; in other words your identifiers cannot start with a number or contain other symbols. This is because the compiler needs a way of distinguishing identifiers from numbers entered directly into the code.

![This syntax diagram shows the language rules for defining an identifier in C/C++.](./bin/syntax-out/cpp/lvl1/identifier.png){#fig:figIdentifierSyntax width=600px}

| Keywords  |           |           |           |           |
| :-------- | :-------- | :-------- | :-------- | :-------- |
| auto      | break     | case      | char      | const     |
| continue  | default   | do        | double    | else      |
| enum      | extern    | float     | for       | goto      |
| if        | int       | long      | register  | return    |
| short     | signed    | sizeof    | static    | struct    |
| switch    | typedef   | union     | unsigned  | void      |
| volatile  | while     |           |           |           |
: Keywords in C/C++. These are identifiers that have special meaning to the language. {#tbl:tblKeywords}

| Examples  |           |           |           |           |
| :-------- | :-------- | :-------- | :-------- | :-------- |
| println   | hello     | test_basic     |   square      | draw_rectangle     |
| play_sound_effect  | open_window   | create_server        | download    | fill_ellipse      |
| PI      | COLOR_RED    | TCP     | HTTP       | MAX_WIDTH      |
| main        | Main       | mAin      | mAIn  | mAIN    |
| draw_hill     | load_image    | refresh_screen    | my_game    | delay    |
| ___    | _a_1_s   | a     | _123  | _my  |
: These are example identifiers you could use to name artefacts in C/C++. {#tbl:tblExampleIdentifiers}

<note>
<header>Notes on Identifiers in C/C++</header>
* In the syntax definition an identifier cannot contain spaces, or special characters other than underscores ( _ ).
* A letter is any alphabetic character (*a* to *z* and *A* to *Z*).
* A digit is a single number (*0* to *9*).
* The **keywords** are identifier that has special meaning to the language. This means you can't use these to name artefacts you create. See [@Tbl:tblKeywords].
* The *example identifiers* give you examples identifiers that can be used to name artefacts you create. See [@Tbl:tblExampleIdentifiers].
* You will use identifiers to select the procedures you want to call, and to name the procedures you create.
* C/C++ is case sensitive so `open_window` is different to `Open_Window`.
</note>

### Program Declaration Syntax: Level 1 ###

To create a program in the C/C++ programming language you need to create a file that contains a **main** procedure somewhere in your source code. [@Fig:figProgramSyntax] shows the structure of the syntax used to create a program using the C/C++ language.

![This is the syntax diagram for creating a program in C/C++.](./bin/syntax-out/cpp/lvl1/program.png){#fig:figProgramSyntax width=600px}


The following code shows an example C/C++ [program](#program_artefact). You should be able to match this up with the syntax defined in [@Fig:figProgramSyntax]. Notice the start the syntax indicates we can have some optional **header includes**, this matches up with the first three lines in the code which *include* some libraries. The trangular brackets are used for standard libraries, like the C/C++ standard IO (stdio.h). The quotes are used to include other libraries, like SplashKit. These header files give you access to a artefacts contained in libraries.

After the header includes, you can declare your own procedures. For this to be a [program](!program_artefact), one of your procedures must be called "main".

```c
#include <stdio.h>
#include "splashkit.h"
#include "splashkit_starter.h"

void main()
{
    printf("Hello...");
    println("World!");
}
```

<note>
<header>Notes on C Program Syntax</header>
* When the program runs, it starts at the first [statement](#statement_terminology) within the *main* function.
* With the *header include* syntax you use triangular brackets (`<...>`) to include the standard C/C++ libraries, and quotes (`"..."`) to include other external libraries (like splashkit).
* At this stage you need to using the splashkit_starter to make this work in C/C++, we will explore this in the next chapter.
</note>

### Procedure Declaration Syntax: Level 1 ###

[@Fig:figProcedureSyntax] shows the syntax for creating your own procedures in C/C++.

![This diagram shows the syntax for creating a procedure in C/C++.](./bin/syntax-out/cpp/lvl1/procedure-decl.png){#fig:figProcedureSyntax width=600px}

The following code includes four procedure declarations.

```c
/// Program: print_steps.c
///
/// Prints out the steps to cook a meal... (partial)

#include "splashkit.h"
#include "splashkit_starter.h"

void find_what_to_cook()
{
    println("Step 1 - Find what to cook -");
    println("1 - Find a recipe book");
    println("2 - Pick recipe ");
}

void purchase_missing_ingredients()
{
  println("Step 2(a) - Purchase Missing Ingredients -");
  println("1 - Goto Shop");
  println("2 - Find ingredients and put in basket");
  println("3 - Go to register and pay for ingredients in basket");
  println("4 - Return home");
}

void get_ingredients()
{
  println("Step 2 - Purchase Ingredients -");
  println("1 - Read recipe");
  println("2 - Write a list of ingredients ");
  println("3 - Check food stocks, and tick off ingredients you already have");
  purchase_missing_ingredients();
}

void main()
{
    find_what_to_cook();
    get_ingredients();
    // etc...
}
```

<note>
<header>Notes on Procedure Declarations</header>
* There are four procedures declared in the above code.
* A *procedure declaration* starts with the keyword `void`. This indicates that the following code is a procedure declaration to the compiler.
* The *procedure name* is an identifier: the name of the [procedure](#procedure_artefact). This can be any valid [identifier](Identifier Syntax) that has not been used before.
* The empty parenthesis must appear after the procedure's name, and before the *block*.
* The *block* contains a list of statements. These are the actions that the procedure gets the computer to perform when it is called.
* Instructions in the *block* are executed in **sequence**.
* There are a number of conventions, called coding standards, that describe how your code should appear for a given language. We will use the C/C++ convention from the standard libraries. In this coding convention, each *procedure name* should be written in **snake_case**.
</note>

### Statement Syntax: Level 1 ###

Each procedure has a list of [statements](#statement_terminology) that tell the computer what actions to perform. Each language supports a few different kinds of statements. At this stage, all of the statements in the C/C++ programs are procedure calls. The syntax for statements will change as you learn how to do more things with code.

![At this stage, statements in C/C++ are procedure calls. The different things you can do will expand as we explore programming further.](./bin/syntax-out/cpp/lvl1/statement.png){#fig:figProcedureCallSyntax width=600px}

<note>
<header>Notes related to statements in C/C++</header>
* At this stage all statements in our programs will be procedure calls.
</note>

### Procedure Call Syntax ###

A [procedure call](#procedure_call_action) allows you to run the code in a [procedure](#procedure_artefact), getting its instructions to run before control returns back to this point in the program.

![This is the syntax for calling a procedure in C/C++.](./bin/syntax-out/cpp/lvl1/procedure-call.png){#fig:figProcedureCallSyntax width=600px}

The following is an example of a procedure call. This line of code will call a procedure named `fill_rectangle`, and passes in five arguments to this procedure's parameters for color, x, y, width and height. If you review the example code in the [procedure declaration syntax](#procedure_declaration_syntax_level_1), it has many example procedure calls.

```c
fill_rectangle(COLOR_RED, 10, 30, 200, 300);
```

<note>
<header>Notes related to procedure calls in C/C++</header>
* The procedure call starts with the procedure's [identifier](#identifier_terminology), which indicates the name of the procedure to be called.
* Following the identifier is a list of values within parenthesis, these are the arguments (coded as [expressions](#expression_terminology)) that are passed to the procedure's parameters for it to use.
* C/C++ is case sensitive so `Fill_Rectangle` is different to `fill_rectangle`.
</note>

### Expression Syntax ###

An [expression](#expression_terminology) in C/C++ is a mathematical calculation or a literal value. Each expression results in a value, of a certain [type](#type_artefact), being calculated when the expression is used. [@Tbl:tblExpressionOperators] lists the operators that you can use in your expressions, in order of precedence. The operators you can use depend on the kind of data that you are using within the expression.

| Operators      | Description    | Example        | Value | Type |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|  `( )`         | Parenthesis, brackets | `(1 + 1) * 2` | 4 | `int` |
|  `% * /`       | Modulo, Multiplication, and Division | | | |
|                | Modulo (remainder after division)    | `10 % 3` | 1 | `int` |
|                |                | `11 % 4`    | 3     | `int` |
|                | Multiplication | `3 * 1.5`   | 4.5   | `double` |
|                |                | `4 * -2`     | -8     | `int` |
|                | Division       | `3 / 1.5`   | 2.0   | `double` |
|                |                | `-3 / 2`     | -1     | `int` |
| `+ -`          | Addition and Subtraction | | | |
|                | Addition       | `1 + 1` | 2 | `int` |
|                |                | `3 + 1.2` | 4.2 | `double` |
|                |                | `-3.1 + 1.2` | -1.9 | `double` |
|                | Subtraction    | `11 - 3` | 8 | `int` |
|                |                | `6 - -1` | 7 | `int` |
|                |                | `7.4 - 3` | 4.4 | `double` |
: Operators in C/C++ with examples related to numeric values. {#tbl:tblExpressionOperators}

### Types and Literals in C/C++ ###

[Types](#type_artefact) are used to define how data is interpreted and the operations that can be performed on that data. This section outlines the standard C/C++ types, and how to represent these values in your code as literals.

![This is the syntax for coding literal values in C/C++.](./bin/syntax-out/cpp/lvl1/literal.png){#fig:figLiteral width=600px}


#### Whole Numbers ####
There are several different integer types in C/C++. Most of the time you will use `int`, but its good to know the options. Each of the options represents the integer value using a number of bytes, the new bytes the larger the value it can store.

* `short` and `unsigned short`
    * Size: 2 bytes/16 bits
    * Signed range: -32,767 .. 32,767
    * Unsigned range: 0 .. 65,536
* `int` and `unsigned int`
    * Size: 4 bytes/32 bits
    * Signed range: -2,147,483,648 .. 2,147,483,647
    * Unsigned range: 0 .. 4,294,967,296
* `long long` and `unsigned long long`
    * Size: 8 bytes/64 bits
    * Signed range: -9,223,372,036,854,775,807 .. 9,223,372,036,854,775,807
    * Unsigned range: 0 .. 18,446,744,073,709,551,615

#### Real Numbers  ####
Real numbes are stored as *floating point* values, which refers to the format used to represent these in binary. The format used to store these values is capable of representing very large and small numbers, but with only a certain number of significant digits. For example, the `float` type can represent a large range of real numbers but with only six significant digits. So, `0.183028302` would become `0.183028`, but it could also be used to represent smaller values such as `0.000000003816`, or much larger values like `820,146,000,000,000`. So the important thing to think about with real numbers is the level of accuracy you require.

* `float`
    * Size: 4 bytes/32 bits
    * Range: 1.0e-38 .. 1.0e38
    * Significant digits: 6
* `double`
    * Size: 8 bytes/64 bits
    * Range: 2.0e-308 .. 2.0e308
    * Significant digits: 10

#### Text          ####
There are two basic categories of text: single characters, and sequences (strings) of characters. In C/C++ the `char` type is used to represent single characters, whereas `string` or `char *` ("*char star*") is used to signify a string.

* `char`
    * Size: 1 byte/8 bits
* `string`
    * Size: varies based on number of characters
* `char *`
    * Size: varies based on number of characters


| Type          |Operators Permitted   | Notes                                                 |
| :------------ | :----------          | :--------------                                       |
| Whole Numbers | ` ( ) + - / * %`     | Division rounds down if all values are whole numbers. |
| Real Numbers  | ` ( ) + - / *`       |                                                       |
| Text          | ` ( ) `              | You cannot perform mathematical operations on text.   |
: C/C++ Permitted Operators by Type {#tbl:tblCPermittedOperators}
