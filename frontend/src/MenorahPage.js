import React, { useState } from 'react';
import Menorah from './Menorah.js';
import ConjugatedTable from './ConjugatedTable.js';

const binyanim = [
  'nifal',
  'pual',
  'hufal',
  'hitpael',
  'hifil',
  'piel',
  'paal',
];

const sampleBatchConjugation = [
  {
    "binyan": "paal",
    "outputword": "\u05db\u05d5\u05b9\u05ea\u05d1",
    "shoresh": "\u05db\u05ea\u05d1",
    "zman": "hoveh"
}
]

function MenorahPage(){

  const [selectedArch, setSelectedArch] = useState();


  return (
    <div className="menorah-page">
      <Menorah onArchClick={setSelectedArch} activeArch={selectedArch} />
      <div>
        {binyanim[selectedArch]}
      </div>
      <ConjugatedTable />

    </div>
  );
}

export default MenorahPage;