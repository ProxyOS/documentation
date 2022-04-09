Architecture
============

There will be obviously a software running on the computer, let's call it the **GatewayManager** from now
and a software running on the gateways, let's call it the **Kernel** from now.

The both will communicate together via some **channels** using a **messaging protocol**.

Channels
--------

For simplicity, only bidirectionnal channel with both ends initiatives will be considered at first glance.

Example of channels to be considered:

* UART
* WiFi/Ethernet/IP:

  * TCP
  * SSL/TCP
  * UDP

* Bluetooth/BLE
* USB
* Zigbee
* LoRa
* CAN
* ...

Example of channels not to be considered:

* SPI (master only initiative)
* I²C (master only initiative)
* 1-Wire (master only initiative)
* ...

In the first version of the architecture, we will consider channels as perfect: no data loss and no
data corruption. `ECC <https://en.wikipedia.org/wiki/Error_correction_code>`_ and acknoledgement
mechanisms might be considered in next versions.

Messaging protocol
------------------

We want something simple to use at code level, efficient and which doesn't imply to introduce a big
complexity in the project structure.

When considering messaging protocol, there is several questions to answer:

1. How do I know the beginning and the end of my message?
2. How do I know which type of message did I receive?
3. How do I parse the message, knowing it's type?
   How much does it cost in term memory and time?
4. What's the information quantity/message size ratio?

.. todo:: Short explanation about common formats from
          `that list <https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats>`_
          and why a zero copy version of BSON as been implemented in C.

Gateway Manager
---------------

.. todo:: List common actions that should be available

.. todo:: Explain peripheral proxy interface declaration

Kernel
------

.. todo:: Explain peripheral driving principle

.. todo:: Explain project architecture and build system policy

.. todo:: Explain the different cases: general purpose board vs dedicated purpose board. Show the interest
          of using device tree in some cases => Level1
