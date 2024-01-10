#!/usr/bin/node
exports.esrever = function (list) {
  let tmp;
  const len = list.length;
  for (let i = 0; i < len / 2; i++) {
    tmp = list[len - i - 1];
    list[len - i - 1] = list[i];
    list[i] = tmp;
  }
  return list;
};
