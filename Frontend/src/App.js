import React, { useCallback, useState, useEffect } from 'react';
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";
import particlesJson from "./particles.json";
import axios from 'axios'

function App() {

    const [particleOject, setParticleObject] = useState('')
    
    const particlesInit = useCallback(main => {
        loadFull(main);
    }, [])

    useEffect(() => {
       const fetchParticles = async() => {
           const res = await axios.get('http://127.0.0.1:5000')
          setParticleObject(res.data)
       }
       fetchParticles()
    },[])

    return (
        <div className="App">
            <Particles options={particleOject} init={particlesInit}/>
        </div>
    );
}

export default App;