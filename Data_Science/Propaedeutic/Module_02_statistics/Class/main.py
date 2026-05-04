#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:56:57 2026

@author: irukandji
"""

import my_first_queue

def main():
    new_queue = my_first_queue.Queue()
    
    new_queue.enqueue(99)
    new_queue.enqueue(55)
    new_queue.enqueue(77)
    print(new_queue)


if __name__ == "__main__":
    main()
    