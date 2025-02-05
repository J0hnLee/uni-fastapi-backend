#!/bin/bash

while getopts "a:b:" opt; do
  case $opt in
    a) paramA="$OPTARG" ;;
    b) paramB="$OPTARG" ;;
    *) echo "使用方法: $0 -a <值> -b <值>"; exit 1 ;;
  esac
done

echo "A: $paramA"
echo "B: $paramB"