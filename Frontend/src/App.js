import React, { useCallback } from 'react';
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";
import particlesJson from "./particles.json";

function App() {
    const particlesInit = useCallback(main => {
        loadFull(main);
    }, [])

    // fetch request to my end point
    // store returned json object into state
    //set that state into options object 

    return (
        <div className="App">
            <Particles options={particlesJson} init={particlesInit}/>
        </div>
    );
}

export default App;