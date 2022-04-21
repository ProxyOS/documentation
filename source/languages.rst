Supported Languages
===================

:repository:`Gateway kernel <kernel>`
-------------------------------------

On gateway side, things have to be small, efficient and compatible with
most of the plateform.
Only pure C match all these requirements, even C++ is not supported correctly
on some plateforms.

:repository:`GatewayManager <gateway-manager>`
----------------------------------------------

For simplicity and to avoid too much work when a new peripheral will be
ported to the project, core will be coded in C++ and automatic an binder for
other languages will be developped for supported languages.
This will ensure coherent API between the different ports of each language.

.. index:: Language automatic binding

The chosen strategy is to declare peripheral API (in headers) using
macros that can be easily parsed from the binding generation program.
The pattern chosen for that is:

.. code-block:: c++

  PERIPHERAL_DECLARE_XXX(arg1, arg2, ..., argN);

Which is really easy to parse. For that, the program only have to tokenize
the header file and then find all the matching sequences. This way, no semantic
parsing of the file is required which ensure the program to remain simple in long
term and avoid the introduction of complex dependencies as LLVM.

All the types used for the API are restrained to those supported by BSON,
which is sufficient to do everything. The list is:

.. table::
  :align: center

  +--------------+--------------------------------+
  | BSON Type    | C++ corresponding types        |
  +==============+================================+
  | BSON_BOOLEAN | (bool)                         |
  +--------------+--------------------------------+
  | BSON_STRING  | (std\:\:string) (char const\*) |
  +--------------+--------------------------------+
  | BSON_INT32   | (int32_t)                      |
  +--------------+--------------------------------+
  | BSON_INT64   | (int64_t)                      |
  +--------------+--------------------------------+
  | BSON_DOUBLE  | (double)                       |
  +--------------+--------------------------------+
  | BSON_BINARY  | (bson\:\:Binary)               |
  +--------------+--------------------------------+
  | BSON_OBJECT  | (bson\:\:Object)               |
  +--------------+--------------------------------+
  | BSON_ARRAY   | (bson\:\:Object)               |
  +--------------+--------------------------------+

The possible API declarations are:

.. table::
  :align: center

  +-----------------------------+---------------------------------------------+
  | Declarator                  | Description                                 |
  +=============================+=============================================+
  | PERIPHERAL_DECLARE_GETTER   | Request an single data from the peripheral  |
  +-----------------------------+---------------------------------------------+
  | PERIPHERAL_DECLARE_SETTER   | Send an single data from the peripheral     |
  +-----------------------------+---------------------------------------------+
  | PERIPHERAL_DECLARE_CALLBACK | Set a callback on peripheral initiative     |
  |                             | data transmission                           |
  +-----------------------------+---------------------------------------------+

The binding tool can be found in
:repofile:`GatewayManager <gateway-manager|tools/binder>`.

You can find how it's built by looking at
:repofile:`GatewayManager <gateway-manager|.gitlab-ci.yml>`.

For a more concrete example, look at the :ref:`study_case:Study Case` section.

C++
"""

As said above, this is the base language of this software part.

.. todo:: Add link to generated documentation of the API

Python
""""""

This is the first language on which automatic binding as been implemented.

.. todo:: explain how to get it and how to look at module documentation


NodeJS
""""""

.. todo:: Give release date


Ruby
""""

.. todo:: Give release date

Lua
"""

.. todo:: Give release date
