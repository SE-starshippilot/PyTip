import algoliasearch from 'algoliasearch/lite';
import { InstantSearch, SearchBox, Hits} from 'react-instantsearch';
import 'instantsearch.css/themes/satellite.css';
const searchClient = algoliasearch('I3FCSXAGH4', 'c5fde93a2f7a558f2f1b51e17a2b76e4');

function Hit({ hit }) {
  return (
    <article>
      <img src={hit.image} alt={hit.name} />
      <p>{hit.categories[0]}</p>
      <h1>{hit.name}</h1>
      <p>${hit.price}</p>
    </article>
  );
}

function App() {
  return (
    <InstantSearch searchClient={searchClient} indexName="PyHint">
      <SearchBox />
      {/* <Hits hitComponent={Hit}/> */}
    </InstantSearch>
  );
}
export default App;