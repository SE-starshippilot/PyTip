import React from "react";
import algoliasearch from "algoliasearch/lite";
import {
  InstantSearch,
  SearchBox,
  Hits,
  Highlight,
  useInstantSearch,
} from "react-instantsearch";
import "instantsearch.css/themes/satellite.css";
import "./App.css";

const searchClient = algoliasearch(
  "I3FCSXAGH4",
  "8ac3471bcdd4f6822277c910be74f64e"
);

function GenerateUrl(hit) {
  let baseUrl = "";
  if (hit.library === "numpy") {
    baseUrl = "https://numpy.org/doc/stable/reference/generated/";
  } else {
    baseUrl = "https://matplotlib.org/stable/api/_as_gen/";
  }
  return baseUrl + hit.funct_name.slice(0, -2) + ".html";
}

function Hit({ hit }) {
  console.log(hit);
  return (
    <>
      <article>
        <a href={GenerateUrl(hit)}>
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
    <>
      <div className="bg_container">
        <img src="/background.jpg" className="bg_image"/>
        <div className="app_name">PyHint</div>
        <div className="app_description">A minimalistic search suggestion for Python Libraries</div>
      </div>
      <div   id="search" >
      <InstantSearch searchClient={searchClient} indexName="PyHint">
        <SearchBox/>
        <EmptyQueryBoundary>
          <NoResultsBoundary>
            <Hits hitComponent={Hit} />
          </NoResultsBoundary>
        </EmptyQueryBoundary>
      </InstantSearch>
      </div>
    </>
  );
}

function EmptyQueryBoundary({ children }) {
  const { indexUiState } = useInstantSearch();

  if (!indexUiState.query) {
    return (
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          marginTop: "200px",
        }}
      >
        <img src="/empty.svg" width={50} height={50} alt="empty" />
        <h1>What is in your mind?</h1>
        <p style={{ textAlign: "center" }}>
          Start typing for suggestions......
        </p>
      </div>
    );
  }

  return children;
}

function NoResultsBoundary({ children }) {
  const { indexUiState } = useInstantSearch();
  console.log(children);
  if (indexUiState.nbHits === 0) {
    return (
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          marginTop: "200px",
        }}
      >
        <img src="/no-results.svg" width={50} height={50} alt="no-results" />
        <h1>No results found</h1>
        <p style={{ textAlign: "center" }}>Try a different query</p>
      </div>
    );
  }

  return children;
}

export default App;
