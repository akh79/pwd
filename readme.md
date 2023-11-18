# Password generator

## Purpose

Passwords are a real headache in the modern world. This project is a study of possible ways how to reduce the burden put on humans.

## Approach

The password generator creates passwords that can be pronounced and not just sequences of various symbols. Another benefit is that you save keystrokes when typing the password. The idea of this approach is borrowed from this website [Passwort Generator](https://passwort-generator.org). The Python implementation is mine. Typical generated passwords look like this:
- dejoropocyfy
- koqesigerupapoli

## Algorithm

The initial algorithm is quite simple:
- generate a random sequence of consonants,
- generate a random sequence of vowels,
- merge two sequences, so that consonants and vowels alternate.

## Implementation

Current implementation generates passwords containing small letters only. The only input parameter is the password length (8 is the lower bound). The module imports two other modules, random and sys. It is tested with Python 12 on Windows only.

## Usage

You can either import the module and then call the function passwordgen(n) or you can execute the script on the command line.

## Possible extensions

Add capital letters, add special symbols, but keep the main idea unchanged.
