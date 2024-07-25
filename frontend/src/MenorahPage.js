import React, { useState } from 'react';
import Menorah from './Menorah.js';

const binyanim = [
  'nifal',
  'pual',
  'hufal',
  'hitpael',
  'hifil',
  'piel',
  'paal',
];

function MenorahPage(){

  const [selectedArch, setSelectedArch] = useState();


  return (
    <div className="menorah-page">
      <Menorah onArchClick={setSelectedArch} activeArch={selectedArch} />
      <div>
        {binyanim[selectedArch]}
      </div>
    </div>
  );
}

export default MenorahPage;