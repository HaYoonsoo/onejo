
const search = (data, value) => {
  const result = [];
  for (const datum of data) {
    if (datum.includes(value)) {
      result.push(datum);
    }
  }
  return result;
}

const searchBar = document.querySelector('.search-bar');
//const selectedPeople = 