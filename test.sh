#!/bin/bash
RED="\033[0;31m"
GREEN="\033[0;32m"
CLEAR="\033[0m"

echo -n "arguments "
ARGUMET_OUT=$(python adventure.py 2>&1)

if [ "$ARGUMET_OUT" = "please provide valid arguments" ] ; then
  echo -e "${GREEN} OK ${CLEAR}"
else
  echo -e "${RED} FAIL ${CLEAR}"
fi

echo -n "map validity "

# checking map
EMPTY_MAP_OUT=$(python adventure.py ./test_map/empty.map 2>&1)
EMPTY__MAP_ERR="map is missing key: 'start', 'rooms'"

INVALID_ROOM_OUT=$(python adventure.py ./test_map/invalid_room.map 2>&1)
INVALID_ROOM_ERR="room '1' is missing key: 'exits'
room '3' is missing key: 'name', 'desc', 'exits'"

DUPLICATE_NAME_OUT=$(python adventure.py ./test_map/duplicate_name.map 2>&1)
DUPLICATE_NAME_ERR_1="duplicate room name: A white room, A blue room"
DUPLICATE_NAME_ERR_2="duplicate room name: A blue room, A white room"

INVALID_EXIT_OUT=$(python adventure.py ./test_map/invalid_exit.map 2>&1)
INVALID_EXIT_ERR="invalid exit: A orange room, A black room"


if [ "$EMPTY_MAP_OUT" = "$EMPTY__MAP_ERR" ] &&
   [ "$INVALID_ROOM_OUT" = "$INVALID_ROOM_ERR" ] &&
   { [ "$DUPLICATE_NAME_OUT" = "$DUPLICATE_NAME_ERR_1" ] || [ "$DUPLICATE_NAME_OUT" = "$DUPLICATE_NAME_ERR_2" ]; } &&
   [ "$INVALID_EXIT_OUT" = "$INVALID_EXIT_ERR" ]; then
    echo -e "${GREEN} OK ${CLEAR}"
else
  echo -e "${RED} FAIL ${CLEAR}"
fi


echo -n "start room "

CHECK_START_ROOM=$(python adventure.py ./test_map/invalid_start.map 2>&1)
CHECK_START_ERR="start room \"A orange room\" don't exist"

if [ "$CHECK_START_ROOM" = "$CHECK_START_ERR" ]; then
  echo -e "${GREEN} OK ${CLEAR}"
else
  echo -e "${RED} FAIL ${CLEAR}"
fi
