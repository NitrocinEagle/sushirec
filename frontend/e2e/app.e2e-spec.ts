import { SushirecFrontendPage } from './app.po';

describe('sushirec-frontend App', function() {
  let page: SushirecFrontendPage;

  beforeEach(() => {
    page = new SushirecFrontendPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
