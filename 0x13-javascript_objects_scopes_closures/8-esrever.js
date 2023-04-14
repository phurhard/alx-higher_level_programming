#!/usr/bin/node
exports.esrever = function (list) {
  const List = [];
  for (let i = (list.length - 1); i >= 0; i--) {
    List.push(list[i]);
  }
  return List;
};
