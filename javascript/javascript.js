document.write("<p>majun</p>")

var a = 3;
var name = "majun"
if (a > 5) {
    alert("large")
} else {
    alert("small")
}

var person = {
    name: "majun",
    age: 15,
    nickname: "mamengli"
};

// alert(person.name)
// alert("I'am \"ok\"")
// alert(`akgf
// ajfalpkg
// ajgplarkg`)

// var message = `my name is ${name}`
// alert(name[0])

var arr = [1, "a", 10]
// arr.push("majun")
// alert(arr.join("-"))

var s = 1
for (var a = 1; a < 11; a++) {
    s *= a
}
alert(s)

for (let i = 0; i < arr.length; i++) {  
    console.log(arr[i])
}

for ( key in person ) {
    if (person.hasOwnProperty(key)) {
        console.log(person.key)
    }
}

var m = new Map()
m.set("majun", 100)
m.set("mamengli", 99)
alert(m.get("majun")) 

var s = new Set()
s.add(1)
console.log(s)

arr.name = "majun"
for (var a of arr) {
    console.log(a)
}

arr.forEach(function (element, index) {
    console.log(element + ', index = ' + index)
})


// 函数 ---------------------------------------------------------


function abs(x) {
    if (typeof x !== 'number') {
        throw 'not a number';
    }
    alert(arguments)
    return x >= 0 ? x : -x
}

console.log(abs(5))

function foo(a,b, ...rest) {
    console.log("a = " + a)
    console.log("b = " + b)
    console.log(rest)
}

foo(1, 2, 3, 4, 5)

function sum(...rest) {
    var b = 0
    for (var t = 0; t < rest.length; t++) {
        b += rest[t]
        console.log(rest[t])
    }
    console.log(b)
}

function sum_1(...rest) {
    var s = 0
    arr.forEach(function (element, index) {
        s += element
        console.log(element)
        console.log(index)
    })
    // console.log(s)
}


sum(500, 100)

sum_1(1,2,3)

var p, r

function area_of_circle(r, p=3.14) {
    return p * p * r
}

console.log(area_of_circle(5, 2))


function foo() {
    var x = 1
    function bar() {
        var x = 'A'
        console.log('x in bar is ' + x)
    }
    console.log('x out bar is ' + x)
    // 内部函数难道需要单独调用吗？
    bar()
}

foo()

// 将变量提升到函数顶部, 但是没有提升变量的值
function fun1() {
    var j = "hello, " + g
    console.log(j)
    var g = "world!"
}

fun1()
// 全局对象 window
window.fun1()

const PI = 3.14


// 方法    绑定到对象上的函数称为方法---------------------------------------------

// this
var majun = {
    name: "mamengli",
    birth: 1996,
    age: function () {
        var y = new Date().getFullYear();
        return y - this.birth;
    }
};

console.log(majun.age)
console.log(majun.age())


var now = new Date()

console.log(now.getDate())

var Student = {
    name:"majun",
    age: 21,
    height: 178,
    skills: ['js', 'python']
}

var s = JSON.stringify(majun, null, ' ')
console.log(s)

var obj = JSON.parse('{"name":"xiaoming", "age":21}', function (key, value) {
    if ( key == "name") {
        return value + "同学"
    }
    return value
})

console.log(obj)


function createStudent(name) {
    var s = Object.create(Student)
    s.name = name
    return s
}

var majun = createStudent("mamengli")
console.log(majun.skills)

function Dog(name) {
    this.name = name
    this.hello = function () {
        return "hello" + this.name + "wawa"
    }
}

weifeichang = new Dog("feichang")
console.log(weifeichang.name)
console.log(weifeichang.hello())

console.log(window.innerWidth)

document.title = "好好学习"
