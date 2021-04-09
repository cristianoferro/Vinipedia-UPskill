import { Route, Switch } from "react-router";
import Nav from "./components/Nav";
import SearchBar from "./components/SearchBar";
import Homepage from "./pages/Homepage";

function App() {
  return (
    <div className="App">
      <Switch>
        <Route path="/" exact>
          <Nav />
          <SearchBar />
          <Homepage />
        </Route>
      </Switch>
    </div>
  );
}

export default App;
