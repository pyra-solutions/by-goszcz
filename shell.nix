{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell rec {
  buildInputs = with pkgs; [
    gcc
    go
    nodejs_22
    air

    # tooling
    gopls
    sqlite
    litecli
    postgresql_16
  ];
}
