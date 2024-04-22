import React, {useState} from 'react';
import './App.css';

function App() {
  const [binyan, setBinyan] = useState();
  const [zman, setZman] = useState();
  const [shemguf, setShemguf] = useState();
  const [shoresh, setShoresh] = useState("כתב");
  const [output, setOutput] = useState();

  const fetchConjugation = ()=>{
    fetch('/conjugate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ shoresh, binyan, zman, shem_guf: shemguf}),
    }).then(res => res.json())
    .then(response => setOutput(response.outputword))
  }


  return (
    <div className="App">
      <header className="App-header">
        <label>
        select binyan:
          <select value={binyan} onChange={e=> setBinyan(e.target.value)}>
            <option value="">select binyan</option>
            <option value="paal">paal</option>
            <option value="piel">piel</option>
            <option value="hifil">hifil</option>
            <option value="hitpael">hitpael</option>
            <option value="nifal">nifal</option>
          </select>
        </label>


        <label>
        select zman:
          <select value={zman} onChange={e=> setZman(e.target.value)}>
            <option value="">select zman</option>
            <option value="hoveh">hoveh</option>
            <option value="avar">avar</option>
            <option value="atid">atid</option>
          </select>
        </label>


        <label>
        select shem guf:
          <select value={shemguf} onChange={e=> setShemguf(e.target.value)}>
            <option value="">select shem guf</option>
            <option value="ani">ani</option>
            <option value="ani">ani (zachar)</option>
            <option value="anin">ani (nekeva)</option>
            <option value="ata">ata</option>
            <option value="at">at</option>
            <option value="hu">hu</option>
            <option value="hi">hi</option>
            <option value="anaxnu">anaxnu</option>
            <option value="atem">atem</option>
            <option value="aten">aten</option>
            <option value="hem">hem</option>
            <option value="hen">hen</option>
          </select>
        </label>

        <label>
        type shoresh:
        <input value={shoresh} onChange={e=> setShoresh(e.target.value)} />
        </label>
        <button onClick={fetchConjugation}>
        conjugate!
        </button>

        <h2>{output}</h2>

        <svg viewBox="0 0 100 100">
        <circle cx={25} cy={25} r={20} fill="#f00" onClick={()=>setBinyan("paal")}/>
        <circle cx={75} cy={75} r={20} fill="#0f0" onClick={()=>console.log(2)}/>
        </svg>

      </header>
    </div>
  );
}

export default App;


//can also style in css
//instead of circle it will be a branch and instead of console.log it will say whatever setBinyan("piel")
//then when you click it it will be the same as selecting from the dropdown

//should be able to render the text for the labels of the menorah
//want a variable for the binyan will do a dropdown and replace later and the same for zman and input for hebrew chatachters and accept at a certain length
//dropdown for binyan, zman, shem_guf and an input box for shoresh
//single button says conjugate and will render the conjugate verb at the bottom
