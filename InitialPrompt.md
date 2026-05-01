# Initial Project Prompt

This file preserves the original repository bootstrap prompt that defined the project direction and initial workflow expectations.

## Original Prompt

> We are working on a project to test and develop my harness engineering skills.
>
> References
>
> First, I would like you to read this article: https://openai.com/index/harness-engineering/
> Second, Look at https://github.com/EricLeeFriedman/CopilotChess for a starting point. I want you to look at the files in the .github folder and AGENTS.md file. While that repository is specific for a Chess game, I want you to extract the information in that .github folder and AGENTS.md file in a generic way to kickstart this project. It has a good starting point for code reviews, retros on pull requests, automation, etc.
>
> The goal of this project is to build a full agentic first pipeline that does the design, coding, review, and submission of code.
>
> Game Information and Requirements
>
> We are making a game of checkers
> The game should be able to be restart after a winner is decided
>
> Application Requirements and Constraints
>
> This will be a Windows app only
> The game requires graphics, and should be done via 2D software rendering using the Windows API
> The game will only need to be played with a mouse. Click and drag to move pieces
> The game will only be played on a single machine, so two players switching off with the mouse
>
> Build System and Source Control
>
> Building the code should be done by a simple .ps1 script that invokes the cl.exe
> You are in a github repository and will be using github for source control
> You can use the tools available to you in github, like the Issues feature to track work
>
> Code Style and Architecture
>
> This is a C++ application
> Do NOT use object oriented programming: Use C-style APIs for boundaries, structs with public variables, etc
> Avoid dynamic memory allocation during runtime. We can allocate a block of memory up front and use that
> The memory should be divided up into separate arenas for different systems
> You will not be using any 3rd party libraries. Avoid the C standard library as well
>
> Testing
>
> Testing should happen in the application. It should be a first class citizen of the application, we are not using a testing harness or a separate application to do unit testing. The application should be able to start up in a testing mode that runs through a suite of tests that you will be creating and maintaining.
>
> Finally, save this initial prompt in a nice markdown file for posterity
>
> This is all I can think of right now. Given these requirements and the above article, we are going to create the initial commit now.
>
> Ask me any questions that will help you make the correct choices. If you are uncertain of something, ask!
> This initial commit should not have code. We are setting up the repo for an agentic first workflow

## Bootstrap Decisions Captured During Setup

- Use the CopilotChess repository as the structural starting point, adapted for checkers and generic workflow automation.
- Keep the initial commit code-free with respect to application and gameplay code.
- Use standard GitHub-hosted runners for agent and review automation now.
- Add Windows-specific build and test workflows later, when `build.ps1` and `src/` exist.
