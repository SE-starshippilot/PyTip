import React, { useEffect, useRef } from 'react';
import { autocomplete } from '@algolia/autocomplete-js';
import '@algolia/autocomplete-theme-classic';

data = require('./mock_data.json');
const SearchPrediction = () => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!containerRef.current) {
      return;
    }

    const search = autocomplete({
      container: containerRef.current,
      getSources() {
        return [
          {
            sourceId: 'predictions',
            getItems() {
              // Implement your logic to fetch search predictions from Algolia or any other data source
              // Return an array of prediction items
              return [
                { label: 'Prediction 1' },
                { label: 'Prediction 2' },
                { label: 'Prediction 3' },
              ];
            },
          },
        ];
      },
      render({ state, collections }) {
        // Implement your rendering logic here
        // Use state and collections to render the autocomplete UI
      },
    });

    return () => {
      search.destroy();
    };
  }, []);

  return <div ref={containerRef} />;
};

export default SearchPrediction;