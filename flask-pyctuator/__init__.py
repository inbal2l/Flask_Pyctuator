import pyctuator

def pyctuator(
    app: Any,
    app_name: str,
    app_url: str,
    pyctuator_endpoint_url: str,
    registration_url: Optional[str],
    registration_auth: Optional[Auth] = None,
    app_description: Optional[str] = None,
    registration_interval_sec: int = 10,
    free_disk_space_down_threshold_bytes: int = 1024 * 1024 * 100,
    logfile_max_size: int = 10000,
    logfile_formatter: str = default_logfile_format,
    auto_deregister: bool = True,
)

    return Pyctuator(
        app,
        app_name,
        app_url,
        pyctuator_endpoint_url,
        registration_url,
        registration_auth,
        app_description,
        registration_interval_sec,
        free_disk_space_down_threshold_bytes,
        logfile_max_size,
        logfile_formatter,
        auto_deregister,
    )
	
	