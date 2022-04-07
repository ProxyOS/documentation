Goals
=====

The main goal of the project is to provide a **simple** and **small-sized** architecture allowing
to control embedded peripherals from a master computer.

The **simple** and **small-sized** adjectives are capital, because it should be easy for a single
experienced person to port the whole set in few days to a new MCU (for the embedded part) or
OS (for the master part).
For this matter, we will restrain the number of features to the strict minimum and put size
limit (in lines) to each part (library, tool...) of the project.
The dependencies should also be as rare as possible. In short, you will have to think lightweight if you
want to be part of the project.

There is a second goal to the project (in relation with the first), which could be resumed as
**"accessibility to the complexity"**.
I personnaly like projects like Arduino or RaspberryPi, and I think that if you read these lines,
you might too.
But I remarked something about these projects by seeing people using them: most of the time they are
introduced to the electronics and software world, but there is a huge gap between their beginner level
and an experienced level, and even if they would like to learn more, the path is really, really not that easy.
Think about it, and look at the Arduino project for example: how do you pass from coding in the IDE using
very high level libraries, not having any idea of what is happening in the backstage, to a point where you
can create an independant project, coding the driver layer that fits your need, on a custom hardware that
you designed?

I'd like this project to have these intermediate steps. It should create a path for people who want to reach
an experienced level, by not only giving tools and software, but also giving several levels of usage and a not
too high difference of altitude between each one of them:

* **Level 1** I never used a microcontroller but I have some notion about programming. I'd like
  to use one to do simple stuff, like in Arduino project, and it should not be painful to set it up.
* **Level 2** I'd like to port a new peripheral to the system. I want more that using high level API and I begin
  to get interest in what happen in the backstage.
* **Level 3** I'd like to port the project to an existing board. I understand better what's under the hood, and now
  I'd like to eat something more spicy.
* **Level 4** I'd like to create a custom board because my needs are not fulfilled with any existing one and then
  port the project on it.
