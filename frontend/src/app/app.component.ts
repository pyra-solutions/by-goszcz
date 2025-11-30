import { Component, OnInit } from '@angular/core';
import { faker } from '@faker-js/faker';

interface Orzeczenie {
  lp: number;
  sygnatura: string;
  dataWydania: Date;
  dataOgloszenia: Date;
  publikator: 'Dz.U.' | 'M.P.';
  rok: number;
  numer: number;
  pozycja: number;
  tytul: string;
  ocenaKonstytucyjnosci: 'zgodny' | 'niezgodny' | 'nie jest niezgodny';
  organWlasciwy: string;
  statusOrzeczenia: string;
}

interface SelectOption {
  label: string;
  value: any;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: false,
})
export class AppComponent implements OnInit {
  title = 'Orzeczenia Trybunału Konstytucyjnego';

  orzeczenia: Orzeczenie[] = [];
  filteredOrzeczenia: Orzeczenie[] = [];

  publikatorOptions: SelectOption[] = [
    { label: '— dowolny —', value: null },
    { label: 'Dz.U.', value: 'Dz.U.' },
    { label: 'M.P.', value: 'M.P.' },
  ];

  ocenaOptions: SelectOption[] = [
    { label: '— dowolna —', value: null },
    { label: 'zgodny', value: 'zgodny' },
    { label: 'niezgodny', value: 'niezgodny' },
    { label: 'nie jest niezgodny', value: 'nie jest niezgodny' },
  ];

  statusOptions: SelectOption[] = [
    { label: '— dowolny —', value: null },
    {
      label: 'Brak konieczności podjęcia prac legislacyjnych',
      value: 'Brak konieczności podjęcia prac legislacyjnych',
    },
    { label: 'Częściowo wykonane', value: 'Częściowo wykonane' },
    { label: 'Niewykonane', value: 'Niewykonane' },
    {
      label: 'Niewykonane / podjęto prace legislacyjne',
      value: 'Niewykonane / podjęto prace legislacyjne',
    },
    { label: 'Wykonane', value: 'Wykonane' },
  ];

  filters = {
    publikator: null as 'Dz.U.' | 'M.P.' | null,
    rok: null as number | null,
    status: null as string | null,
    ocena: null as string | null,
    sygnatura: '',
    fragmentTytulu: '',
  };

  lata: SelectOption[] = [];

  ngOnInit(): void {
    this.initYears();
    this.generateFakeData(200);
    this.applyFilters();
  }

  private initYears() {
    const currentYear = new Date().getFullYear();
    this.lata = [{ label: '— dowolny —', value: null }];

    for (let y = currentYear; y >= currentYear - 20; y--) {
      this.lata.push({ label: y.toString(), value: y });
    }
  }

  private generateFakeData(count: number) {
    const organy = [
      'Minister Sprawiedliwości',
      'Minister Finansów',
      'Minister Zdrowia',
      'Minister Infrastruktury',
      'Minister Rozwoju',
      'Prezes Rady Ministrów',
      'Rada Ministrów',
      'Minister Rodziny, Pracy i Polityki Społecznej',
    ];

    const statusy = this.statusOptions.map((o) => o.value).filter((v): v is string => !!v);

    const oceny: Orzeczenie['ocenaKonstytucyjnosci'][] = [
      'zgodny',
      'niezgodny',
      'nie jest niezgodny',
    ];

    for (let i = 1; i <= count; i++) {
      const rok = faker.number.int({ min: 2010, max: new Date().getFullYear() });
      const dataWydania = faker.date.between({
        from: `${rok}-01-01`,
        to: `${rok}-12-31`,
      });
      const dataOgloszenia = faker.date.between({
        from: dataWydania,
        to: `${rok}-12-31`,
      });

      const publikator: Orzeczenie['publikator'] = faker.helpers.arrayElement(['Dz.U.', 'M.P.']);

      const orzeczenie: Orzeczenie = {
        lp: i,
        sygnatura: `${faker.string.alpha({ length: 1, casing: 'upper' })} ${faker.number.int({
          min: 1,
          max: 50,
        })}/${faker.number.int({ min: 10, max: 25 })}`,
        dataWydania,
        dataOgloszenia,
        publikator,
        rok,
        numer: faker.number.int({ min: 1, max: 3000 }),
        pozycja: faker.number.int({ min: 1, max: 4000 }),
        tytul: faker.lorem.sentence({ min: 5, max: 12 }),
        ocenaKonstytucyjnosci: faker.helpers.arrayElement(oceny),
        organWlasciwy: faker.helpers.arrayElement(organy),
        statusOrzeczenia: faker.helpers.arrayElement(statusy),
      };

      this.orzeczenia.push(orzeczenie);
    }
  }

  applyFilters() {
    this.filteredOrzeczenia = this.orzeczenia.filter((o) => {
      if (this.filters.publikator && o.publikator !== this.filters.publikator) {
        return false;
      }

      if (this.filters.rok && o.rok !== this.filters.rok) {
        return false;
      }

      if (this.filters.status && o.statusOrzeczenia !== this.filters.status) {
        return false;
      }

      if (this.filters.ocena && o.ocenaKonstytucyjnosci !== this.filters.ocena) {
        return false;
      }

      if (
        this.filters.sygnatura &&
        !o.sygnatura.toLowerCase().includes(this.filters.sygnatura.toLowerCase())
      ) {
        return false;
      }

      if (
        this.filters.fragmentTytulu &&
        !o.tytul.toLowerCase().includes(this.filters.fragmentTytulu.toLowerCase())
      ) {
        return false;
      }

      return true;
    });
  }

  resetFilters() {
    this.filters = {
      publikator: null,
      rok: null,
      status: null,
      ocena: null,
      sygnatura: '',
      fragmentTytulu: '',
    };
    this.applyFilters();
  }

  getStatusSeverity(status: string): 'success' | 'info' | 'warning' | 'danger' | 'secondary' {
    switch (status) {
      case 'Wykonane':
        return 'success';
      case 'Częściowo wykonane':
        return 'info';
      case 'Niewykonane':
        return 'danger';
      case 'Niewykonane / podjęto prace legislacyjne':
        return 'warning';
      default:
        return 'secondary';
    }
  }
}
