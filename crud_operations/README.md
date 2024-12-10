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

O comando find usand operador de igualdade retorna documentos que possuam o valor escalar do campo igual ao valor especificado, ou que contenha o valor especificado presente dentro de um Array.

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

## Replace de documentos em uma collection

A saída do comando abaixo ilustra a quantidade de documentos cujo conteúdo corresponde ao filtro utilizado no comando.

````BAsh
db.books.replaceOne({_id: ObjectId("aaaa")}, {novo_documento})
````

## Atualização de documentos em uma collection

Sintaxe geral:

````Bash
db.collection.updateOne(
    <filter>,
    <update>,
    <options>
)
````

Dentro do `update`, podemos utilizar métodos como `$set` e `$push`:

- $set:
    - Cria novos campos e valores dentro do documento caso não existam
    - Ou atualizam valores de campos no documento caso existam
    - Neste operador, `upsert: true` indica que o mongo deve inserir um novo documento na collection com as informações caso o filtro não retorne nenhum documento
- $push:
    - Adiciona um novo valor a um Array caso o array já exista
    - Ou cria um novo Array com o valor definido como elemento 