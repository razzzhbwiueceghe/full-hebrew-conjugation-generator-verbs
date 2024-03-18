# hebrew pealim

## project structure

 - server side flask python
 - front end react javascript

## goals

create an application that generates the correct conjugation of hebrew verbs
 when selected letters of the shoresh are entered and the binyan
 is selected as well

```
fetch('/conjugate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ shoresh: 'אכל' , binyan: 'pual', zman: 'avar'}),
}).then(res => res.json())
.then(response => console.log(response))
```
