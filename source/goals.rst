Goals
=====

The main goal of the project is to provide a **simple** and **small-sized** architecture allowing
to :important:`control embedded peripherals from a master computer`.

.. index:: Network abstract description

.. graphviz::
  :align: center

  graph abstract {
    rankdir="LR"
    node [ fontname="Lucida Grande" ]
    edge [ fontname="Lucida Grande" ]

    subgraph Computer {
      rank=same
      node [ shape=component, style=filled, fillcolor="#f97c7c" ]
      pc [label="computer"]
    }

    subgraph Gateway {
      rank=same
      node [ shape=box, style=filled, fillcolor="#82bcf2" ]
      g1 [label="gateway1"]
      gx [label="gateway..."]
      gn [label="gatewayN"]
    }

    subgraph Peripheral {
      rank=same
      node [ shape=octagon, style=filled, fillcolor="#81e896" ]

      p1   [label="peripheral1"]
      p2   [label="peripheral2"]
      p3   [label="peripheral3"]
      p4   [label="peripheral4"]
      p5   [label="peripheral5"]
      px   [label="peripheral..."]
      pn_1 [label="peripheralN-1"]
      pn   [label="peripheralN"]
    }

    pc -- { g1 gx gn }

    g1 -- { p1 p2 p3 }
    gx -- { p4 p5 }
    gn -- { px pn_1 pn }
  }

This mean that you should be able to drive a bunch of peripherals with your computer (that it
cannot natively handle via its ports), using some gateways (which are simply microcontrollers) connected
to your computer. A practical example could be:

.. index:: Network practical example

.. graphviz::
  :align: center

  graph abstract {
    rankdir="LR"
    node [ fontname="Lucida Grande" ]
    edge [ fontname="Lucida Grande" ]

    subgraph Computer {
      rank=same
      node [ shape=component, style=filled, fillcolor="#f97c7c" ]
      pc [label="Laptop"]
    }

    subgraph Gateway {
      rank=same
      node [ shape=box, style=filled, fillcolor="#82bcf2" ]
      g1 [label="Arduino Uno"]
      gx [label="Nucleo H7A3ZI"]
      gn [label="ESP32 S3"]
    }

    subgraph Peripheral {
      rank=same
      node [ shape=octagon, style=filled, fillcolor="#81e896" ]

      p1   [label="LED"]
      p2   [label="Servo1"]
      p3   [label="Servo2"]
      p4   [label="Proximity\nSensor"]
      p5   [label="Relay"]
      px   [label="Bipolar\nStepper"]
      pn_1 [label="Robot\nArm"]
      pn   [label="IR\nReceiver"]
    }

    pc -- g1 [label="UART"]
    pc -- gx [label="Eth/TCP"]
    pc -- gn [taillabel="WiFi/TCP", labeldistance=8]

    g1 -- { p1 p2 p3 }
    gx -- { p4 p5 }
    gn -- { px pn_1 pn }
  }

The **simple** and **small-sized** adjectives are capital, because it should be easy for a single
experienced person to port the whole set in few days to a new MCU (for the embedded part) or
OS (for the master part).
For this matter, we will restrain the number of features to the strict minimum and put size
limit (in lines) to each part (library, tool...) of the project.
The dependencies should also be as rare as possible. In short, you will have to think lightweight if you
want to be part of the project.

There is a second goal to the project (in relation with the first one), which could be resumed as
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
an experienced level in the embedded system world, by not only giving tools and software, but also giving
several levels of usage and a not too high difference of altitude between each one of them:

.. index:: User levels

* **Level 1** I never used a microcontroller but I have some notion about programming. I'd like
  to use one to do simple stuff, like in Arduino project, and it should not be painful to set it up.
* **Level 2** I'd like to port a new peripheral to the system. I want more that using high level API and I begin
  to get interest in what happens in the backstage.
* **Level 3** I'd like to port the project to an existing board. I understand better what's under the hood, and now
  I'd like to eat something more spicy.
* **Level 4** I'd like to create a custom board because my needs are not fulfilled with any existing one and then
  port the project on it.
