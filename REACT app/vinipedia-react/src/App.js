import Nav from "./components/Nav";
import Homepage from "./components/Homepage";
import axios from "axios";
import {useEffect} from 'react';
import { useDispatch, useSelector } from "react-redux";
import loadActionAsync from './actions/load-action';
import WineList from './components/WineList';

function App() {

  const dispatch = useDispatch()

  const wineData = useSelector(state => state.load.wines)
  console.log("winedata",wineData)

  useEffect(() =>{
    dispatch(loadActionAsync());
  },[dispatch])

  return (
    <div className="App">
      <WineList wineData={wineData} />
    </div>
  );
}

export default App;
