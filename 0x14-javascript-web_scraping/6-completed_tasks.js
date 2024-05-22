#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (body) {
    const allTodos = JSON.parse(body);
    const userData = {};
    for (const eachTodo in allTodos) {
      const currentUser = String(allTodos[eachTodo].userId);
      const curUserTodoState = allTodos[eachTodo].completed;
      if (!(currentUser in userData)) {
        userData[currentUser] = 0;
      }
      if (curUserTodoState === true) {
        userData[currentUser]++;
      }
    }
    const filteredUsers = {};
    for (const curUser in userData) {
      if (userData[curUser] > 0) {
        filteredUsers[curUser] = userData[curUser];
      }
    }
    console.log(filteredUsers);
  }
});
