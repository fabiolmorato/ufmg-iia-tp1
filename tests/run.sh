#!/bin/bash

cd ..;

run-tests() {
  ALGORITHM=$1;
  if [[ $ALTERNATE_HEURISTIC = "True" ]]; then
    ALGORITHM="$1_ALTERNATE";
  fi

  echo "Running tests for algorithm $ALGORITHM...";

  mkdir -p results/$ALGORITHM;
  for i in $(seq 0 $2); do
    echo "└── Running test $i...";
    (time python3 src/main.py $1 $(cat toys/$i.txt) PRINT) > results/$ALGORITHM/$i 2>&1;
  done
}

run-tests A 24
ALTERNATE_HEURISTIC=True run-tests A 16
run-tests B 14
run-tests G 16
ALTERNATE_HEURISTIC=True run-tests G 16
run-tests I 14
run-tests H 16
run-tests U 11
