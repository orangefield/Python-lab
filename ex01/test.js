// spread로 부분 수정, 삭제 등을 쉽게 할 수 있다.
list1 = [1,2,3]
console.log(list1)

list1 = [...list1, 4] // spread
console.log(list1)

// cos의 id를 2로 변경하고 싶다, username을 ssar로 변경하고 싶다
let user = {
    id:1,
    username:"cos"
}
// user = {...user, id:2} 
// console.log(user);

user = {...user, username:"ssar"}
console.log(user);

