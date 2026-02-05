#!/usr/bin/env node

// Entertainment tracking script
// Checks tours and local venues, generates digest

const artists = [
  { name: 'Bill Burr', url: 'https://punchup.live/billburr/tickets', type: 'comedy' },
  { name: 'Wolf Alice', url: 'https://wolfalice.co.uk/#tour', type: 'music' },
  { name: 'Foo Fighters', url: 'https://www.foofighters.com/tour-dates/', type: 'music' },
  { name: 'Metallica', url: 'https://www.metallica.com/tour/', type: 'music' },
  { name: 'Guns n Roses', url: 'https://www.gunsnroses.com/tour', type: 'music' },
  { name: 'Rachel Feinstein', url: 'https://rachel-feinstein.com', type: 'comedy', friend: true },
  { name: 'April Macie', url: 'http://aprilmacie.com/#TOUR', type: 'comedy', friend: true }
];

const citiesOfInterest = [
  'Washington', 'D.C.', 'DC',
  'New York', 'NYC', 'NY',
  'Paris',
  'Vienna',
  'Miami',
  'London'
];

const localVenues = [
  { name: 'DC Improv', url: 'https://www.dcimprov.com/', type: 'comedy' },
  { name: 'Capitol One Arena', url: 'https://www.capitalonearena.com/events', type: 'venue' },
  { name: '9:30 Club', url: 'https://www.930.com/', type: 'music' },
  { name: 'Washington Capitals', url: 'https://www.nhl.com/capitals/schedule', type: 'sports' },
  { name: 'Blues Alley', url: 'https://www.bluesalley.com/', type: 'music' },
  { name: 'Jazz in the Garden', url: 'https://www.nga.gov/calendar/jazz-in-garden.html', type: 'music', seasonal: 'summer' }
];

console.log('Entertainment Tracking Script');
console.log('============================\n');
console.log('Artists to check:', artists.length);
console.log('Venues to check:', localVenues.length);
console.log('\nThis is a placeholder - will be integrated with browser automation');
