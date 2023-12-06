import React from 'react';
import algoliasearch from 'algoliasearch/lite';
import { InstantSearch, SearchBox, Hits, Highlight, useInstantSearch } from 'react-instantsearch';
import 'instantsearch.css/themes/satellite.css';

const searchClient = algoliasearch('I3FCSXAGH4', '8ac3471bcdd4f6822277c910be74f64e');

function GenerateUrl(hit) {
  let baseUrl = '';
  if (hit.library === 'numpy') {
    baseUrl = 'https://numpy.org/doc/stable/reference/generated/';
  } else {
    baseUrl = 'https://matplotlib.org/stable/api/_as_gen/';
  }
  return baseUrl + hit.funct_name.slice(0, -2) + '.html';
}

function Hit({ hit }) {
  console.log(GenerateUrl(hit));
  return (
    <>
      <article>
        <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html">
          <h2>{hit.funct_name}</h2>
        </a>
        <p>
          <Highlight attribute="funct_description" hit={hit} />
        </p>
      </article>
    </>
  );
}

function App() {
  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        marginTop: '10%',
      }}
    >
      <div
        style={{
          width: '60%',
        }}
      >
        <InstantSearch searchClient={searchClient} indexName="PyHint">
          <SearchBox id="search" />
          <EmptyQueryBoundary>
            <Hits hitComponent={Hit} />
          </EmptyQueryBoundary>
        </InstantSearch>
      </div>
    </div>
  );
}

function EmptyQueryBoundary({ children }) {
  const { indexUiState } = useInstantSearch();

  if (!indexUiState.query) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '200px' }}>
        <img src='/empty.svg' width={50} height={50}/>
        <h1>What is in your mind?</h1>
        <p style={{ textAlign: 'center' }}>Start typing for suggestions......</p>
      </div>
    );
  }

  return children;
}

export default App;