## Inserindo documentos na collection

Comando para inserir um único documento na collection:

````Bash
db.grades.insertOne( {student_id: 546799, scores: [{type: "quiz", score: 50}, {type: "homework", score: 70}]} )
````

Comando para inserir múltiplos documentos na collection:

````Bash
db.grades.insertMany([{student_id: 1111, scores: [{type: "quiz", score: 50}, {type: "homework", score: 70}]}, {student_id: 2222}])
````

## Buscando documentos na collection

Para filtrar os documentos de uma collection, usamos o método ````find````

````Bash
db.grades.find()
````

Para filtrar os documetos de uma collection filtrando pela igualdade de um atributo, podemos passar o campo e o valor que desejamos que sejam iguais nos documentos:

````Bash
db.grades.find( {student_id: 1111} )
````

Podemos utilizar o ````$in```` para filtrar todos os documentos cujos valores dos campos estejam presentes dentro de uma lista de valores pré-definida:

````Bash
db.grades.find( {student_id: {$in: [111, 222]}} )
````

Podemos filtrar documentos utilizando os operadores `$gt`, `$lt`, `$gte`, `lte`

````Bash
db.sales.find( {"items.price": {"$gt": 100}} )
````

````Bash
db.sales.find( {"items.price": {"$lt": 100}} )
````

````Bash
db.sales.find( {"items.price": {"$gt": 100}} )
````

````Bash
db.sales.find( {"items.price": {"$lte": 100}} )
````

````Bash
db.sales.find( {"items.price": {"$gte": 100}} )
````