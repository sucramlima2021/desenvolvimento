def get_diff(history_record):
    """
    Retorna as diferenças entre a versão atual (history_record)
    e a versão anterior (history_record.prev_record).
    """
    diffs = {}
    prev = history_record.prev_record

    if not prev:
        return diffs  # primeira versão, não há diff

    for field in history_record._meta.fields:
        field_name = field.name
        if field_name in ["id", "history_id", "history_date", "history_type", "history_user"]:
            continue

        old_value = getattr(prev, field_name, None)
        new_value = getattr(history_record, field_name, None)

        if old_value != new_value:
            diffs[field.verbose_name] = {
                "old": old_value,
                "new": new_value
            }

    return diffs
