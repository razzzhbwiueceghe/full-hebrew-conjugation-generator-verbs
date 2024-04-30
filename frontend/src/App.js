import React, {useState} from 'react';
import './App.css';

function App() {
  const [binyan, setBinyan] = useState();
  const [zman, setZman] = useState();
  const [shemguf, setShemguf] = useState();
  const [shoresh, setShoresh] = useState("כתב");
  const [output, setOutput] = useState();

  const fetchConjugation = ()=>{
    const shem_guf = (
      ["avar", "atid"].includes(zman)&&
      ["aniz", "anin", "anaxnuz", "anaxnun"].includes(shemguf)
    )?(shemguf.substr(0, shemguf.length-1)):(shemguf);

    fetch('/conjugate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ shoresh, binyan, zman, shem_guf}),
    }).then(res => res.json())
    .then(response => setOutput(response.outputword))
  }


  return (
    <div className="App">
      <header className="App-header">
        <label>
        select binyan:
          <select value={binyan} onChange={e=> setBinyan(e.target.value)}>
            <option value="">תבחר בניין</option>
            <option value="paal">פעל</option>
            <option value="piel">פיעל</option>
            <option value="hifil">הפעיל</option>
            <option value="hitpael">התפעל</option>
            <option value="nifal">נפעל</option>
          </select>
        </label>


        <label>
        select tense:
          <select value={zman} onChange={e=> setZman(e.target.value)}>
            <option value="">תבחר זמן</option>
            <option value="hoveh">הווה</option>
            <option value="avar">עבר</option>
            <option value="atid">עתיד</option>
          </select>
        </label>


        <label>
        select pronoun:
          <select value={shemguf} onChange={e=> setShemguf(e.target.value)}>
            <option value="">תבחר שם גוף</option>
            <option value="aniz">אני (זכר)</option>
            <option value="anin">אני (נקבה)</option>
            <option value="ata">אתה</option>
            <option value="at">את</option>
            <option value="hu">הוא</option>
            <option value="hi">היא</option>
            <option value="anaxnuz">אנחנו (זכר)</option>
            <option value="anaxnun">אנחנו (נקבה)</option>
            <option value="atem">אתם</option>
            <option value="aten">אתן</option>
            <option value="hem">הם</option>
            <option value="hen">הן</option>
          </select>
        </label>

        <label>
        type root:
        <input value={shoresh} onChange={e=> setShoresh(e.target.value)} />
        </label>
        <button onClick={fetchConjugation}>
        conjugate!
        </button>


        <h2>{output}</h2>



    </header>
  </div>

);
}


export default App;
//<svg viewBox="0 0 100 100">
//<circle cx={25} cy={25} r={20} fill="#f00" onClick={()=>setBinyan("paal")}/>
//<circle cx={75} cy={75} r={20} fill="#0f0" onClick={()=>console.log(2)}/>
//</svg>

//can also style in css
//instead of circle it will be a branch and instead of console.log it will say whatever setBinyan("piel")
//then when you click it it will be the same as selecting from the dropdown

//should be able to render the text for the
//want a variable for the binyan will do a dropdown and replace later and the same for zman and input for hebrew chatachters and accept at a certain length
//dropdown for binyan, zman, shem_guf and an input box for shoresh
//single button says conjugate and will render the conjugate verb at the bottom
