# `axiom`

A minimal Matrix Homeserver implementation for testing and prototyping.

It's objective is to provide a codebase that is easy for developers to fork and iterate prototyping

It is not intended to be a heavily-used or stable homeserver implementation, the focus is an easy gate into a matrix
feature, stability and master-branch compatibility with the matrix spec and ecosystem comes second.

*Licensed under the EUPL*

## Structure

Most/all `axiom` classes are intended to be subclassed and implemented for experimental purposes, but there are a few
pointers to its intended structure and operational boundaries;

`axiom.network` contains code for communication, this communication can be capsuled, redirected, or sub-implemented (
e.g. `axiom.network.http`), but no logic happens here.

`axiom.server` contains code pertaining to the real "meat and bones" of a matrix server, the "logic".

`axiom.storage` contains code for storage and retrieval.

All classes provided are intended to be abstract, default implementations may be provided, but ultimately, the goal is
to provide a generic framework for matrix-server-oriented prototyping, with specialization in those three sub-modules.
