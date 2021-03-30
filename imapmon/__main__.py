from .scripts import run


def main():
    return run(auto_envvar_prefix='IMAPMON')  # pylint: disable=no-value-for-parameter


if __name__ == '__main__':
    main()
