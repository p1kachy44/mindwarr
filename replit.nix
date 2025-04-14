{pkgs}: {
  deps = [
    pkgs.postgresql
    pkgs.openssl
    pkgs.python39Packages.python-telegram-bot
  ];
}
